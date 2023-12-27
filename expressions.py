"""
An expression is a binary tree. Unlike `tree.py` 
it contains data as well as having structure.

Each leaf is a number.
Each non-leaf node is an operator.

e.g. 

     * 
    / \
   3   -
      / \
     4   1


or ( 3 * ( 4 - 1 ) ), i.e. 9 




"""

from fractions import Fraction
from operator import add, sub, mul, truediv

from trees import size

operators = {"*": mul, "+": add, "-": sub, "/": truediv}


def expression(numbers, operators, tree):
    """
    Create an expression from a given list of numbers,
    a list of operators, and a tree structure.
    """
    assert size(tree) == len(numbers)
    assert size(tree) == len(numbers) == len(operators) + 1
    n = size(tree)

    if n == 1:
        assert tree == None
        return numbers[0]
    else:
        assert isinstance(tree, tuple)
        left_tree, right_tree = tree
        ll, lr = size(left_tree), size(right_tree)
        split = size(left_tree)

        assert ll + lr == len(numbers)

        left_ops, op, right_ops = (
            operators[0 : split - 1],
            operators[split - 1],
            operators[split:],
        )
        left_numbers, right_numbers = numbers[0:split], numbers[split:]

        return (
            expression(left_numbers, left_ops, left_tree),
            op,
            expression(right_numbers, right_ops, right_tree),
        )


def repr(expression):
    match expression:
        case int() as i:
            return f"{i}"
        case Fraction() as f:
            return f"{f}"
        case (left, operator, right):
            assert operator in operators
            return f"( {repr(left)} {operator} {repr(right)} )"

    raise ValueError(f"{expression} cannot be represented ")


def evaluate(expression):
    match expression:
        case int() as i:
            return Fraction(i, 1)
        case Fraction() as f:
            return f
        case (left, operator, right):
            op = operators[operator]
            return op(evaluate(left), evaluate(right))
    raise ValueError(f"{expression} cannot be evaluated")


def test_01():
    v = evaluate(Fraction(10, 5))
    assert v == Fraction(2, 1)
    assert v == 2


def test_02():
    v = evaluate((1, "+", 2))
    assert v == 3


def test_03():
    v = evaluate((1, "+", (2, "*", 3)))
    assert v == 7


def test_04():
    e = expression([1, 2, 3], ["+", "-"], (None, (None, None)))

    assert repr(e) == "( 1 + ( 2 - 3 ) )"
    assert evaluate(e) == 0
