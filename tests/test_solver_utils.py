from typing import Dict

import pytest
from pulp import LpProblem, value

from src.utagmsengine.utils.solver_utils import SolverUtils


@pytest.fixture()
def performance_table_list_dummy():
    return [[26.0, 40.0, 44.0],
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
            [62.0, 43.0, 0.0]]

@pytest.fixture()
def preferences_list_dummy():
    return [
        [6, 5],
        [5, 4]
    ]


@pytest.fixture()
def indifferences_list_dummy():
    return [
        [3, 6]
    ]


@pytest.fixture()
def weights_list_dummy():
    return [0.4, 0.25, 0.35]


@pytest.fixture()
def problem_variable_values_dummy():
    return [0.18666667, 0.0, 0.46666667, 0.46666667, 0.0, 0.46666667, 0.46666667, 0.46666667, 0.0, 0.46666667, 0.0, 0.46666667, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.53333333, 0.0, 0.53333333, 0.53333333, 0.53333333, 0.53333333, 0.53333333, 0.53333333, 0.53333333]


@pytest.fixture()
def necessary_dummy():
    return [['A', 'C'], ['A', 'E'], ['A', 'F'], ['A', 'J'], ['A', 'K'], ['C', 'J'], ['D', 'B'], ['D', 'C'], ['D', 'E'], ['D', 'F'], ['D', 'G'], ['D', 'H'], ['D', 'J'], ['D', 'K'], ['F', 'E'], ['F', 'J'], ['G', 'B'], ['G', 'C'], ['G', 'D'], ['G', 'E'], ['G', 'F'], ['G', 'H'], ['G', 'J'], ['G', 'K'], ['I', 'B'], ['K', 'C'], ['K', 'J'], ['L', 'J']]


@pytest.fixture()
def direct_relations_dummy():
    return {'A': {'F', 'K'}, 'C': {'J'}, 'D': {'G'}, 'F': {'E', 'J'}, 'G': {'B', 'H', 'D', 'F', 'K'}, 'I': {'B'}, 'K': {'C'}, 'L': {'J'}}


def test_create_variables_list_and_dict(performance_table_list_dummy):
    u_arr, u_arr_dict = SolverUtils.create_variables_list_and_dict(performance_table_list_dummy)

    assert len(u_arr) == 3
    assert len(u_arr_dict) == 3
    assert len(u_arr[0]) == 11
    assert len(u_arr[1]) == 10
    assert len(u_arr[2]) == 10
    assert u_arr[0][0].name == 'u_0_0.0'
    assert u_arr_dict[0][26.0].name == 'u_0_26.0'


def test_calculate_epsilon(
    performance_table_list_dummy,
    preferences_list_dummy,
    indifferences_list_dummy,
    weights_list_dummy,
    problem_variable_values_dummy
):
    problem: LpProblem = SolverUtils.calculate_epsilon(
        performance_table_list=performance_table_list_dummy,
        preferences=preferences_list_dummy,
        indifferences=indifferences_list_dummy,
        weights=weights_list_dummy,
        alternative_id_1=1,
        alternative_id_2=2
    )

    variable_values = []
    for var in problem.variables():
        variable_values.append(value(var))

    assert variable_values == problem_variable_values_dummy


def test_calculate_direct_relations(necessary_dummy, direct_relations_dummy):
    direct_relations: Dict[str, set] = SolverUtils.calculate_direct_relations(necessary_dummy)

    assert direct_relations == direct_relations_dummy
