import unittest
from nose.tools import *
from polygon import Polygon

class PointInsidePolygonTestCase(unittest.TestCase):
    def test_should_retrive_each_side_that_crosses_the_Y_from_the_test_point(self):
        A = [3, 6]; B = [3, 11]; C = [6, 11]; D = [6, 9]; E = [5, 9]; F = [5, 6]
        polygon = Polygon([A, B, C, D, E, F])
        test_point = [4, 7]
        assert_equals(polygon.get_number_of_intersected_sides(test_point), {"left" : 1, "right" : 1}) #note that the the vertical side CD must not to be returned

    def test_should_retrieve_false_to_a_point_that_is_not_inside_a_polygon(self):
        A = [3, 6]; B = [3, 11]; C = [6, 11]; D = [6, 9]; E = [5, 9]; F = [5, 6]
        polygon = Polygon([A, B, C, D, E, F])
        test_point = [4, 5]
        assert_false(polygon.belongs_to_polygon(test_point))
        test_point = [6, 7]
        assert_false(polygon.belongs_to_polygon(test_point))

    def test_should_retrieve_true_to_a_point_that_is_inside_a_polygon(self):
        A = [3, 6]; B = [3, 11]; C = [6, 11]; D = [6, 9]; E = [5, 9]; F = [5, 6]
        polygon = Polygon([A, B, C, D, E, F])
        test_point = [4, 7]
        assert_true(polygon.belongs_to_polygon(test_point))

    def test_should_retrieve_false_to_a_point_that_is_not_inside_a_more_complex_polygon(self):
        A = [1, 2]; B = [1, 4]; C = [3, 4]; D = [3, 6]; E = [5, 6];
        F = [5, 4]; G = [7, 4]; H = [7, 6]; I = [9, 6]; J = [9, 2]
        polygon = Polygon([A, B, C, D, E, F, G, H, I, J])
        test_point = [6, 5]
        assert_false(polygon.belongs_to_polygon(test_point))

    def test_should_retrieve_true_to_a_point_that_is_inside_a_more_complex_polygon(self):
        A = [1, 2]; B = [1, 4]; C = [3, 4]; D = [3, 6]; E = [5, 6];
        F = [5, 4]; G = [7, 4]; H = [7, 6]; I = [9, 6]; J = [9, 2]
        polygon = Polygon([A, B, C, D, E, F, G, H, I, J])
        test_point = [5, 5]
        assert_true(polygon.belongs_to_polygon(test_point))

    def test_should_retrieve_false_to_a_point_outside_a_polygon_that_has_6_sides(self):
        A = [2, 1]; B = [2, 5]; C = [4, 5]
        D = [4, 8]; E = [6, 8]; F = [6, 1]
        polygon = Polygon([A, B, C, D, E, F])
        test_point = [2, 8]
        assert_false(polygon.belongs_to_polygon(test_point))
