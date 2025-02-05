import time
time.sleep(10)
import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, ys", [
    ([], []),
    ([1], [1]),
    ([1], [2]),
    ([], [3, 2, 1]),
    ([4, 2], [1, 3]),
])
def test_concatenate(xs, ys):
    copy_xs = xs[:]
    copy_ys = ys[:]
    student.concatenate(copy_xs, copy_ys)

    assert ys == copy_ys, 'ys should remain unchanged'
    assert copy_xs == [*xs, *ys]


@pytest.mark.timeout(1)
def test_concatenate_with_same_object():
    xs = [1, 2, 3]
    student.concatenate(xs, xs)

    assert [1, 2, 3, 1, 2, 3] == xs


class NaughtyStudentException(Exception):
    pass


class DummyList(list):
    def __iadd__(self, x):
        raise NaughtyStudentException()


@pytest.mark.timeout(1)
def test_concatenate_does_not_use_pluseqe():
    lst = DummyList([1, 2, 3])
    try:
        student.concatenate(lst, [4, 5, 6])
    except NaughtyStudentException:
        assert False, "Don't use += to implement this function"
