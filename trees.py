"""
A tree here is simply a binary tree. 

i.e. a tree is either a tuple (tree, tree) or None.

It contains no data, just structure

In `expressions.py` we use a given tree structure to create an expression
"""


def repr(tree):
    assert isinstance(tree, tuple) or tree is None, f"{tree} is not a tree"
    match tree:
        case [left, right]:
            return f"({repr(left)},{repr(right)})"
        case None:
            return "*"

    raise ValueError()


def size(tree):
    assert isinstance(tree, tuple) or tree is None
    match tree:
        case [left, right]:
            return size(left) + size(right)
        case None:
            return 1
    raise ValueError()


def generate(N):
    assert N > 0
    if N == 1:
        yield None

    for i in range(1, N):
        for left_tree in generate(i):
            for right_tree in generate(N - i):
                yield (left_tree, right_tree)


def test_01():
    tree = (None, ((None, None), None))
    s = repr(tree)

    assert s == "(*,((*,*),*))"


def test_02():
    tree = (None, ((None, None), None))
    assert size(tree) == 4
