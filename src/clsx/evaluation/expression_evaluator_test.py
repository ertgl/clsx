__all__ = ["ExpressionEvaluatorTest"]

from itertools import chain
from typing import cast
from unittest import TestCase

from clsx.abc import (
    CallableExpression,
    ClassName,
    DictExpression,
    Expression,
    ExpressionList,
    ExpressionSet,
)
from clsx.contrib.itertools import dedup
from clsx.contrib.stdlib import RepresentableLambda
from clsx.evaluation.expression_evaluator import ExpressionEvaluator


class ExpressionEvaluatorTest(TestCase):
    BLANK = str()

    SPACE = " "

    CLASS_NAMES_LIST = ["nice", "nice--better"]

    CLASS_NAMES_STR = str.join(SPACE, CLASS_NAMES_LIST)

    WHITESPACES_LIST = [SPACE, "\f", "\n", "\r", "\t", "\v"]

    WHITESPACES_STR = str.join("", WHITESPACES_LIST)

    STR_DATA: list[tuple[ClassName, str]] = [
        (BLANK, BLANK),
        (CLASS_NAMES_STR, CLASS_NAMES_STR),
        (f" {CLASS_NAMES_STR} {CLASS_NAMES_STR} ", CLASS_NAMES_STR),
        (WHITESPACES_STR, BLANK),
    ]

    LIST_DATA: list[tuple[ExpressionList, str]] = [
        ([expression, expression, expression, expression], expected)
        for expression, expected in STR_DATA
    ]

    SET_DATA: list[tuple[ExpressionSet, str]] = [
        (set(expression), expected) for expression, expected in LIST_DATA
    ]

    LAZY_DATA: list[tuple[CallableExpression, str]] = [
        (cast(CallableExpression, RepresentableLambda(expression)), expected)
        for expression, expected in chain(
            STR_DATA,
            LIST_DATA,
        )
    ]

    DICT_DATA: list[tuple[DictExpression, str]] = list(
        chain(
            map(
                lambda kv: ({kv[0]: True}, kv[1]),
                chain(
                    STR_DATA,
                    LAZY_DATA,
                ),
            ),
            map(
                lambda kv: ({kv[0]: False}, ""),
                chain(
                    STR_DATA,
                    LAZY_DATA,
                ),
            ),
        ),
    )

    def evaluate(
        self,
        expression: Expression,
    ) -> str:
        return str.join(
            self.SPACE,
            dedup(
                ExpressionEvaluator.evaluate(
                    expression,
                ),
            ),
        )

    def test_evaluating_str(self) -> None:
        for expression, expected in self.STR_DATA:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(
                    self.evaluate(expression),
                    expected,
                )

    def test_evaluating_list(self) -> None:
        for expression, expected in self.LIST_DATA:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(
                    self.evaluate(expression),
                    expected,
                )

    def test_evaluating_set(self) -> None:
        for expression, expected in self.SET_DATA:
            with self.subTest(expression=expression, expected=expected):
                self.assertSetEqual(
                    set(self.evaluate(expression).split(self.SPACE)),
                    set(expected.split(self.SPACE)),
                )

    def test_evaluating_lazy(self) -> None:
        for expression, expected in self.LAZY_DATA:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(
                    self.evaluate(expression),
                    expected,
                )

    def test_evaluating_dict(self) -> None:
        for expression, expected in self.DICT_DATA:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(
                    self.evaluate(expression),
                    expected,
                )
