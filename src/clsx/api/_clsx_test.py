__all__ = ["ClsxTest"]

from unittest import TestCase

from clsx.api._clsx import clsx


class ClsxTest(TestCase):
    def test_readme_usage_section_examples(self) -> None:
        self.assertEqual(clsx(), "")
        self.assertEqual(clsx(""), "")
        self.assertEqual(clsx("foo"), "foo")
        self.assertEqual(clsx("foo foo"), "foo")
        self.assertEqual(clsx("foo \n\t foo"), "foo")

        self.assertEqual(clsx("foo", None), "foo")
        self.assertEqual(clsx("foo", None, "bar"), "foo bar")

        self.assertEqual(clsx("foo", None, "bar", None), "foo bar")
        self.assertEqual(clsx("foo", None, "bar", None, "baz"), "foo bar baz")

        self.assertEqual(clsx("foo", False), "")
        self.assertEqual(clsx("foo", True), "foo")

        self.assertEqual(clsx("foo", "bar"), "foo bar")
        self.assertEqual(clsx("foo", "bar", "baz"), "foo bar baz")
        self.assertEqual(clsx("foo", "bar", "baz", "qux"), "foo bar baz qux")

        self.assertEqual(clsx(["foo", "bar"]), "foo bar")
        self.assertEqual(clsx(["foo", "bar"], ["baz", "qux"]), "foo bar baz qux")

        self.assertEqual(clsx([("foo", True), ("foo", "bar", "baz")]), "foo bar baz")

        self.assertEqual(clsx(["foo foo"], "foo", "bar"), "foo bar")
        self.assertEqual(clsx("foo", ["foo", "bar", "baz"]), "foo bar baz")

        self.assertEqual(clsx({"foo": True, "bar": False}), "foo")
        self.assertEqual(clsx({"foo": True, "bar": True}), "foo bar")
        self.assertEqual(clsx({(lambda: "foo"): True}), "foo")

        self.assertEqual(clsx(lambda: [lambda: ("foo", True)]), "foo")
