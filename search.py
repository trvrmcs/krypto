from itertools import product, permutations
import trees
from expressions import expression, evaluate

ops = ["+", "-", "*", "/"]


def expressions(numbers, target):
    assert len(numbers) == 5
    N = len(numbers)

    for operators in product(ops, repeat=N - 1):
        for tree in trees.generate(N):
            for permutation in permutations(numbers):
                e = expression(permutation, operators, tree)
                try:
                    v = evaluate(e)
                except ZeroDivisionError:
                    continue
                if v == target:
                    yield e
