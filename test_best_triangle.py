from pytest import approx
from best_triangle import compute_triangle_area


def test_compute_triangle_area():
    assert compute_triangle_area(5,6) == 15
