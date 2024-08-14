__all__ = ["ExpressionEvaluator"]

from typing import (
    Iterable,
    cast,
)

from clsx.abc import (
    BoolCondition,
    CallableCondition,
    CallableExpression,
    ClassNameIterable,
    Condition,
    ConditionalExpressionTuple,
    DictExpression,
    Expression,
    ExpressionIterable,
    ExpressionTuple,
    VariadicExpressionTuple,
)
from clsx.parsing import ClassNameParser


class ExpressionEvaluator:
    @staticmethod
    def evaluate(
        expression: Expression,
    ) -> ClassNameIterable:
        yield from ExpressionEvaluator.evaluate_dynamic(expression)

    @staticmethod
    def evaluate_dynamic(
        expression: Expression,
    ) -> ClassNameIterable:
        if expression is None:
            yield from []
        elif isinstance(expression, str):
            yield from ExpressionEvaluator.evaluate_str(expression)
        elif isinstance(expression, tuple):
            yield from ExpressionEvaluator.evaluate_tuple(expression)
        elif isinstance(expression, dict):
            yield from ExpressionEvaluator.evaluate_dict(expression)
        elif isinstance(expression, list):
            yield from ExpressionEvaluator.evaluate_iterable(expression)
        elif isinstance(expression, set):
            yield from ExpressionEvaluator.evaluate_iterable(expression)
        elif isinstance(expression, Iterable):
            yield from ExpressionEvaluator.evaluate_iterable(
                cast(
                    ExpressionIterable,
                    expression,
                ),
            )
        elif callable(expression):
            yield from ExpressionEvaluator.evaluate_callable(expression)

    @staticmethod
    def evaluate_str(
        expression: str,
    ) -> ClassNameIterable:
        yield from ClassNameParser.parse(expression)

    @staticmethod
    def evaluate_tuple(
        expression: ExpressionTuple,
    ) -> ClassNameIterable:
        if len(expression) == 2:
            yield from ExpressionEvaluator.evaluate_conditional_expression_tuple(
                cast(
                    ConditionalExpressionTuple,
                    expression,
                ),
            )
        else:
            yield from ExpressionEvaluator.evaluate_variadic_expression_tuple(
                cast(
                    VariadicExpressionTuple,
                    expression,
                ),
            )

    @staticmethod
    def evaluate_conditional_expression_tuple(
        expression: ConditionalExpressionTuple,
    ) -> ClassNameIterable:
        sub_expression, condition = expression
        flag = ExpressionEvaluator.evaluate_maybe_condition(condition)
        is_flag_bool = isinstance(flag, bool)
        if not is_flag_bool or flag:
            yield from ExpressionEvaluator.evaluate_dynamic(sub_expression)
            if not is_flag_bool:
                yield from ExpressionEvaluator.evaluate_dynamic(
                    cast(
                        Expression,
                        flag,
                    ),
                )

    @staticmethod
    def evaluate_variadic_expression_tuple(
        expression: VariadicExpressionTuple,
    ) -> ClassNameIterable:
        yield from ExpressionEvaluator.evaluate_iterable(expression)

    @staticmethod
    def evaluate_dict(
        expression: DictExpression,
    ) -> ClassNameIterable:
        for key, value in expression.items():
            yield from ExpressionEvaluator.evaluate_tuple((key, value))

    @staticmethod
    def evaluate_iterable(
        expression: ExpressionIterable,
    ) -> ClassNameIterable:
        for sub_expression in expression:
            yield from ExpressionEvaluator.evaluate_dynamic(sub_expression)

    @staticmethod
    def evaluate_callable(
        expression: CallableExpression,
    ) -> ClassNameIterable:
        yield from ExpressionEvaluator.evaluate_dynamic(expression())

    @staticmethod
    def evaluate_maybe_condition(
        maybe_condition: Condition | Expression,
    ) -> BoolCondition | Expression:
        if callable(maybe_condition):
            return ExpressionEvaluator.evaluate_maybe_condition(maybe_condition())
        elif isinstance(maybe_condition, bool):
            return ExpressionEvaluator.evaluate_bool_condition(maybe_condition)
        return maybe_condition

    @staticmethod
    def evaluate_condition(
        condition: Condition,
    ) -> bool:
        if callable(condition):
            return ExpressionEvaluator.evaluate_lazy_condition(condition)
        return ExpressionEvaluator.evaluate_bool_condition(condition)

    @staticmethod
    def evaluate_lazy_condition(
        condition: CallableCondition,
    ) -> bool:
        return ExpressionEvaluator.evaluate_condition(condition())

    @staticmethod
    def evaluate_bool_condition(
        condition: BoolCondition,
    ) -> bool:
        return not not condition
