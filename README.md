# clsx

Easily define conditional class attributes for HTML elements.

## Motivation

Defining conditional class attributes based on a state can be cumbersome and
error-prone with string concatenation. `clsx` provides a utility function to
handle this logic efficiently, bringing the popular idea from the JavaScript
ecosystem to the Python ecosystem.

## Installation

The package is available on PyPI and can be installed using `pip`.

```bash
pip install clsx
```

## Usage

The `clsx` function takes any number of arguments and returns a string that can
be used as the value of the `class` attribute of an HTML element.

```python
from clsx import clsx

clsx()                                        # ""
clsx("")                                      # ""
clsx("foo")                                   # "foo"
clsx("foo foo")                               # "foo"
clsx("foo \n\t foo")                          # "foo"

clsx("foo", None)                             # "foo"
clsx("foo", None, "bar")                      # "foo bar"

clsx("foo", None, "bar", None)                # "foo bar"
clsx("foo", None, "bar", None, "baz")         # "foo bar baz"

clsx("foo", False)                            # ""
clsx("foo", True)                             # "foo"

clsx("foo", "bar")                            # "foo bar"
clsx("foo", "bar", "baz")                     # "foo bar baz"
clsx("foo", "bar", "baz", "qux")              # "foo bar baz qux"

clsx(["foo", "bar"])                          # "foo bar"
clsx(["foo", "bar"], ["baz", "qux"])          # "foo bar baz qux"
clsx([("foo", True), ("foo", "bar", "baz")])  # "foo bar baz"

clsx(["foo foo"], "foo", "bar")               # "foo bar"
clsx("foo", ["foo", "bar", "baz"])            # "foo bar baz"

clsx({"foo": True, "bar": False})             # "foo"
clsx({"foo": True, "bar": True})              # "foo bar"
clsx({(lambda: "foo"): True})                 # "foo"

clsx(lambda: [lambda: ("foo", True)])         # "foo"
```

### Low-level API

The core of the implementation is the methods in the `ExpressionEvaluator`
class. For each type of input, there is a corresponding method that evaluates
the input and returns an iterator of class names. These methods are designed to
be chained together to form the final iterable.

For optimal performance and memory consumption, `ExpressionEvaluator` consists
of several `generator` methods that yield the class names one by one, as they
are consumed. This allows the evaluation process to be done lazily, which is
especially useful when dealing with large/infinite and/or nested inputs. Since
the evaluation is done lazily, the both the CPU and memory usage are kept to a
minimum.

```python
from clsx.evaluation import ExpressionEvaluator

output_stream = ExpressionEvaluator.evaluate(input_stream)
```

#### Modularity

The implementation supports on-the-fly modifications of class names out of the
box by its nature. For more complex use cases similar to deduplication,
[CSS Modules](https://github.com/css-modules/css-modules) resolution or
anything else, the low-level API can be extended by chaining the output
iterable with other `generator` functions. This allows for a modular design
where each step of the evaluation process can be customized and extended
independently, with zero extra overhead.

For an example of how to extend the low-level API, see the `deduplication`
section below.

#### Deduplication

The deduplication is always enabled when using the high-level API. However, when
using the low-level API, the deduplication must be done manually. This can be
achieved by using the `dedup` function from the `clsx.contrib.itertools`
module, which is a generator function that deduplicates the input stream without
ahead of planning or buffering. See the example below.

```python
from clsx.contrib.itertools import dedup
from clsx.evaluation import ExpressionEvaluator

output_stream = ExpressionEvaluator.evaluate(input_stream)
deduplicated_output_stream = dedup(output_stream)
```

#### CSS Modules

The `CSS Modules` resolution is not supported out of the box, but can be
achieved by modifying the output stream by chaining it with a custom generator
function that resolves the class names. See the example below.

```python
from clsx.abc import ClassNameIterable
from clsx.evaluation import ExpressionEvaluator

STYLES = {"foo": "Zm9v"}

def resolve_css_module_class_names(
    iterable: ClassNameIterable,
) -> ClassNameIterable:
    for class_name in iterable:
        yield STYLES.get(class_name, class_name)

output_stream = ExpressionEvaluator.evaluate(input_stream)
resolved_output_stream = resolve_css_module_class_names(output_stream)
```

## Inspiration

This project is inspired by the popular idea implemented and widely used in the
JavaScript ecosystem. The name `clsx` is a positive nod to the project
[clsx](https://github.com/lukeed/clsx) by [@lukeed](https://github.com/lukeed),
which provides a similar functionality for JavaScript.

The name `clsx` in this project is used as a shorthand for "class expression"
and it might be pronounced as "classics".

## License

This project is licensed under the
[MIT License](https://spdx.org/licenses/MIT.html).

See the [LICENSE](https://github.com/ertgl/clsx/blob/main/LICENSE) file
for more information.
