import pytest

from src.utagmsengine.solver import Solver
from src.utagmsengine.dataclasses import Preference, Indifference, Criterion


@pytest.fixture()
def performance_table_list_dummy():
    return {
        'A': {'g1': 26.0, 'g2': 40.0, 'g3': 44.0},
        'B': {'g1': 2.0, 'g2': 2.0, 'g3': 68.0},
        'C': {'g1': 18.0, 'g2': 17.0, 'g3': 14.0},
        'D': {'g1': 35.0, 'g2': 62.0, 'g3': 25.0},
        'E': {'g1': 7.0, 'g2': 55.0, 'g3': 12.0},
        'F': {'g1': 25.0, 'g2': 30.0, 'g3': 12.0},
        'G': {'g1': 9.0, 'g2': 62.0, 'g3': 88.0},
        'H': {'g1': 0.0, 'g2': 24.0, 'g3': 73.0},
        'I': {'g1': 6.0, 'g2': 15.0, 'g3': 100.0},
        'J': {'g1': 16.0, 'g2': 9.0, 'g3': 0.0},
        'K': {'g1': 26.0, 'g2': 17.0, 'g3': 17.0},
        'L': {'g1': 62.0, 'g2': 43.0, 'g3': 0.0}
    }


@pytest.fixture()
def preferences_dummy():
    return [Preference(superior='G', inferior='F'), Preference(superior='F', inferior='E')]


@pytest.fixture()
def indifferences_dummy():
    return [Indifference(equal1='D', equal2='G')]


@pytest.fixture()
def criterions_dummy():
    return [Criterion(criterion_id='g1', weight=0.4, gain=True), Criterion(criterion_id='g2', weight=0.25, gain=True), Criterion(criterion_id='g3', weight=0.35, gain=True)]


@pytest.fixture()
def number_of_points_dummy():
    return [3, 3, 3]


@pytest.fixture()
def hasse_diagram_dict_dummy():
    return {'A': {'K', 'F'}, 'C': {'J'}, 'D': {'G'}, 'F': {'E', 'J'}, 'G': {'B', 'D', 'F', 'K', 'H'}, 'I': {'B'}, 'K': {'C'}, 'L': {'H', 'J'}}


@pytest.fixture()
def predefined_hasse_diagram_dict_dummy():
    return {'A': {'F', 'K', 'H'}, 'C': {'J'}, 'D': {'G'}, 'E': {'J'}, 'F': {'C', 'E'}, 'G': {'F', 'I', 'H', 'D'}, 'H': {'B'}, 'I': {'B', 'K', 'E'}, 'K': {'C'}, 'L': {'F', 'I', 'H'}}


@pytest.fixture()
def ranking_dict_dummy():
    return {'E': 0.0, 'B': 0.15, 'H': 0.15, 'C': 0.2, 'J': 0.2, 'I': 0.35, 'F': 0.4, 'K': 0.4, 'L': 0.4, 'A': 0.55, 'D': 0.8, 'G': 0.8}


@pytest.fixture()
def predefined_linear_segments_ranking_dict_dummy():
    return {'B': 0.1498207741935484, 'J': 0.2338110268817204, 'H': 0.29691233333333333, 'C': 0.3070544677419355, 'E': 0.3182838, 'K': 0.40233756451612906, 'F': 0.470739, 'I': 0.5017741559139784, 'A': 0.5122490645161291, 'L': 0.6090455, 'D': 0.623194, 'G': 0.623194}


def test_get_hasse_diagram_dict(
        performance_table_list_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy,
        hasse_diagram_dict_dummy
):
    solver = Solver(show_logs=True)

    hasse_diagram_list = solver.get_hasse_diagram_dict(
        performance_table_list_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy
    )

    assert hasse_diagram_list == hasse_diagram_dict_dummy


def test_get_ranking_dict(
        performance_table_list_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy,
        ranking_dict_dummy,
):
    solver = Solver(show_logs=True)

    ranking = solver.get_ranking_dict(
        performance_table_list_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy
    )

    assert ranking == ranking_dict_dummy


def test_predefined_get_ranking_dict(
        performance_table_list_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy,
        number_of_points_dummy,
        predefined_linear_segments_ranking_dict_dummy
):
    solver = Solver(show_logs=True)

    ranking_predefined_number_of_linear_segments = solver.get_ranking_dict(
        performance_table_list_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy,
        number_of_points_dummy
    )

    assert ranking_predefined_number_of_linear_segments == predefined_linear_segments_ranking_dict_dummy


def test_predefined_get_hasse_diagram_dict(
        performance_table_list_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy,
        number_of_points_dummy,
        predefined_hasse_diagram_dict_dummy
):
    solver = Solver(show_logs=True)

    hasse_diagram_list = solver.get_hasse_diagram_dict(
        performance_table_list_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy,
        number_of_points_dummy
    )

    assert hasse_diagram_list == predefined_hasse_diagram_dict_dummy
