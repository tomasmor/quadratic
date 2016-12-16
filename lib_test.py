import math
import logging
from quadraticlib import solve_equation

epsilon = 10.0e-06

logging.basicConfig(filename="log.txt", level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestQuadraticLib(object):
    def get_roots(self, a, b, c):
        logger.info("Calculatung roots using python")
        if abs(a) < epsilon:
            logger.info("First coefficient is close to zero, it's not a quadratic equation")
            return 1, (0.0, 0.0)
        else:
            discr = b**2 - 4*a*c
            logger.info("Discriminant is %s", discr)
            if discr > 0:
                x1 = (-b + math.sqrt(discr))/(2*a)
                x2 = (-b - math.sqrt(discr))/(2*a)
                logger.info("Roots of quadratic equation are %s %s", x1, x2)
                return 0, (x1, x2)
            elif discr == 0:
                x1 = (-b + math.sqrt(discr))/(2*a)
                x2 = x1
                logger.info("Roots of quadratic equation are %s %s", x1, x2)
                return 0, (x1, x2)
            else:
                return 2, (0.0, 0.0)

    def is_floats_equal(self, a, b):
        return abs(a-b) <= epsilon

    def is_roots_equal(self, tuple_a, tuple_b):
        if tuple_a[0] != tuple_b[0]:
            print tuple_a, tuple_b
            return False
        else:
            if (self.is_floats_equal(tuple_a[1][0], tuple_b[1][0]) and self.is_floats_equal(tuple_a[1][1], tuple_b[1][1])):
                return True
            elif (self.is_floats_equal(tuple_a[1][0], tuple_b[1][1]) and self.is_floats_equal(tuple_a[1][1], tuple_b[1][0])):
                return True
            else:
                return False

    def test_check_roots(self, coefficients):
        a, b, c = coefficients
        logger.info("Starting test case with coefficients a = %s,  b = %s c = %s", a, b, c)
        lib_roots = solve_equation(a, b, c)
        python_roots = self.get_roots(a, b, c)
        assert self.is_roots_equal(lib_roots, python_roots), "Results are different"
