import time
time.sleep(10)
import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('child_count', [1, 2, 5, 10, 14, 19, 200])
@pytest.mark.parametrize('candy_count', [0, 1, 3, 5, 17, 23, 29, 51, 99, 131, 292, 1000])
def test_candy_per_child(child_count, candy_count):
    actual = student.candy_per_child(candy_count=candy_count, child_count=child_count)

    assert candy_count - actual * child_count >= 0, f"candy_per_child({child_count}, {candy_count}) is overly generous and claims that each child gets {actual} pieces of candy"
    assert candy_count - (actual + 1) * child_count < 0, f"candy_per_child({child_count}, {candy_count}) returned {actual}, seemingly withhold candy from the poor children"
