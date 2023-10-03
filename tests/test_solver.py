import pytest

from src.utagmsengine.solver import Solver


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
def alternatives_id_list_dummy():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']


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
def criteria_list_dummy():
    return [1, 1, 1]


@pytest.fixture()
def number_of_points_dummy():
    return [3, 3, 3]


@pytest.fixture()
def hasse_diagram_dict_dummy():
    return {'A': {'K', 'F'}, 'C': {'J'}, 'D': {'G'}, 'F': {'E', 'J'}, 'G': {'B', 'D', 'F', 'K', 'H'}, 'I': {'B'}, 'K': {'C'}, 'L': {'H', 'J'}}


@pytest.fixture()
def predefined_hasse_diagram_dict_dummy():
    return {'A': {'H', 'F', 'K'}, 'C': {'J'}, 'D': {'G'}, 'E': {'J'}, 'F': {'C', 'E'}, 'G': {'F', 'I', 'K', 'H'}, 'H': {'B'}, 'I': {'B', 'C', 'E'}, 'K': {'C'}, 'L': {'H', 'I'}}


@pytest.fixture()
def ranking_dict_dummy():
    return {'E': 0.0, 'B': 0.15, 'H': 0.15, 'C': 0.2, 'J': 0.2, 'I': 0.35, 'F': 0.4, 'K': 0.4, 'L': 0.4, 'A': 0.55, 'D': 0.8, 'G': 0.8}


@pytest.fixture()
def predefined_linear_segments_ranking_dict_dummy():
    return {'J': 0.22921145956989247, 'B': 0.3758064516129032, 'C': 0.379029164516129, 'E': 0.38874960000000003, 'H': 0.42153094666666663, 'I': 0.46968764150537634, 'F': 0.4976204, 'K': 0.503254970967742, 'L': 0.5534433933333334, 'G': 0.716129, 'A': 0.7816814843010753, 'D': 0.825}


def test_get_hasse_diagram_dict(
        performance_table_list_dummy,
        alternatives_id_list_dummy,
        preferences_list_dummy,
        indifferences_list_dummy,
        weights_list_dummy,
        criteria_list_dummy,
        hasse_diagram_dict_dummy
):
    solver = Solver(show_logs=True)

    hasse_diagram_list = solver.get_hasse_diagram_dict(
        performance_table_list_dummy,
        alternatives_id_list_dummy,
        preferences_list_dummy,
        indifferences_list_dummy,
        weights_list_dummy,
        criteria_list_dummy
    )

    assert hasse_diagram_list == hasse_diagram_dict_dummy


def test_get_ranking_dict(
        performance_table_list_dummy,
        alternatives_id_list_dummy,
        preferences_list_dummy,
        indifferences_list_dummy,
        weights_list_dummy,
        criteria_list_dummy,
        number_of_points_dummy,
        ranking_dict_dummy,
):
    solver = Solver(show_logs=True)

    ranking = solver.get_ranking_dict(
        performance_table_list_dummy,
        alternatives_id_list_dummy,
        preferences_list_dummy,
        indifferences_list_dummy,
        weights_list_dummy,
        criteria_list_dummy
    )

    assert ranking == ranking_dict_dummy


def test_predefined_get_ranking_dict(
        performance_table_list_dummy,
        alternatives_id_list_dummy,
        preferences_list_dummy,
        indifferences_list_dummy,
        weights_list_dummy,
        criteria_list_dummy,
        number_of_points_dummy,
        predefined_linear_segments_ranking_dict_dummy
):
    solver = Solver(show_logs=True)

    ranking_predefined_number_of_linear_segments = solver.get_ranking_dict(
        performance_table_list_dummy,
        alternatives_id_list_dummy,
        preferences_list_dummy,
        indifferences_list_dummy,
        weights_list_dummy,
        criteria_list_dummy,
        number_of_points_dummy
    )

    assert ranking_predefined_number_of_linear_segments == predefined_linear_segments_ranking_dict_dummy


def test_predefined_get_hasse_diagram_dict(
        performance_table_list_dummy,
        alternatives_id_list_dummy,
        preferences_list_dummy,
        indifferences_list_dummy,
        weights_list_dummy,
        criteria_list_dummy,
        number_of_points_dummy,
        predefined_hasse_diagram_dict_dummy
):
    solver = Solver(show_logs=True)

    hasse_diagram_list = solver.get_hasse_diagram_dict(
        performance_table_list_dummy,
        alternatives_id_list_dummy,
        preferences_list_dummy,
        indifferences_list_dummy,
        weights_list_dummy,
        criteria_list_dummy,
        number_of_points_dummy
    )

    assert hasse_diagram_list == predefined_hasse_diagram_dict_dummy
