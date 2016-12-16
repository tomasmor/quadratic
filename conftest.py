import math

import pytest
from lxml import etree


def get_parameters():
    tree = etree.parse("config.xml")
    coefficients = [node.text.split() for node in tree.xpath("coefficients")]
    return coefficients

@pytest.fixture(params=get_parameters())
def coefficients(request):
    a = float(request.param[0])
    b = float(request.param[1])
    c = float(request.param[2])
    return a, b, c
