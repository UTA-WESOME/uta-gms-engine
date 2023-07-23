import pytest
import numpy as np

from src.utagms.parser import Parser

from typing import List


@pytest.fixture()
def performance_table_array_dummy():
    return np.array([[26.0, 40.0, 44.0],
                     [2.0, 2.0, 68.0],
                     [18.0, 17.0, 14.0],
                     [35.0, 62.0, 25.0],
                     [7.0, 55.0, 12.0],
                     [25.0, 30.0, 12.0],
                     [9.0, 62.0, 88.0],
                     [0.0, 24.0, 73.0],
                     [6.0, 15.0, 100.0],
                     [16.0, 9.0, 0.0],
                     [26.0, 17.0, 17.0],
                     [62.0, 43.0, 0.0]])


def test_get_performance_table_array(performance_table_array_dummy):
    parser: Parser = Parser()
    performance_table_array: np.ndarray = parser.get_performance_table_array('performance_table.xml')

    assert np.array_equal(performance_table_array, performance_table_array_dummy)
