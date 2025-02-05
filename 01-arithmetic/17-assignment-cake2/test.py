import time
time.sleep(10)
import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("eggs", range(0, 100, 3))
@pytest.mark.parametrize("flour", range(0, 1000, 40))
def test_cake2(eggs, flour):
    eggs_per_cake = 5
    flour_per_cake = 250
    actual = student.cake2(eggs=eggs, flour=flour)

    assert actual * eggs_per_cake <= eggs, f"cake2({eggs}, {flour}) returned {actual}, overestimating the number of cakes"
    assert actual * flour_per_cake <= flour, f"cake2({eggs}, {flour}) returned {actual}, overestimating the number of cakes"
    assert (actual + 1) * eggs_per_cake > eggs or (actual + 1) * flour_per_cake > flour, f"cake2({eggs}, {flour}) returned {actual}, underestimating the number of cakes"
