import time
time.sleep(10)
import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('x', range(-10, 10))
@pytest.mark.parametrize('y', range(-10, 10))
def test_average(x, y):
    actual = student.average(x, y)

    assert 2 * actual == x + y, f'average({x}, {y}) wrongly returns {actual}'
