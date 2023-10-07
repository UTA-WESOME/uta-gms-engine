import pytest
from src.utagmsengine.dataclasses import Preference, Indifference, Criterion, DataValidator


@pytest.fixture()
def performance_table_list_dummy():
    return {
        'A': {'g1': 26.0, 'g2': 40.0, 'g4': 44.0},
        'B': {'a1': 2.0, 'g2': 2.0, 'g4': 68.0},
        'C': {'g1': 18.0, 'g2': 17.0, 'g4': 14.0},
        'D': {'g1': 35.0, 'g2': 62.0, 'g4': 25.0},
        'E': {'g1': 7.0, 'g2': 55.0, 'g4': 12.0},
        'F': {'g1': 25.0, 'g2': 30.0, 'g4': 12.0},
        'G': {'g1': 9.0, 'g2': 62.0, 'g4': 88.0},
        'H': {'g1': 0.0, 'g2': 24.0, 'g4': 73.0},
        'I': {'g1': 6.0, 'g2': 15.0, 'g4': 100.0},
        'J': {'g1': 16.0, 'g2': 9.0, 'g4': 0.0},
        'K': {'g1': 26.0, 'g2': 17.0, 'g4': 17.0},
        'L': {'g1': 62.0, 'g2': 43.0, 'g4': 0.0}
    }


@pytest.fixture()
def preferences_list_dummy():
    return [
        {'superior': 'G', 'inferior': 'F'},
        {'superior': 'F', 'inferior': 'E'},
    ]


@pytest.fixture()
def indifferences_list_dummy():
    return [
        {'equal1': 'D', 'equal2': 'G'}
    ]


@pytest.fixture()
def criterion_list_dummy():
    return [
        {'criterion_id': 'g1', 'weight': 0.4, 'gain': True},
        {'criterion_id': 'g2', 'weight': 0.25, 'gain': True},
        {'criterion_id': 'g3', 'weight': 0.35, 'gain': True},
    ]


@pytest.fixture()
def preferences_dummy():
    return [Preference(superior='G', inferior='F'), Preference(superior='F', inferior='E')]


@pytest.fixture()
def indifferences_dummy():
    return [Indifference(equal1='D', equal2='G')]


@pytest.fixture()
def criterions_dummy():
    return [Criterion(criterion_id='g1', weight=0.4, gain=True), Criterion(criterion_id='g2', weight=0.25, gain=True), Criterion(criterion_id='g3', weight=0.35, gain=True)]


def test_preferences(
        preferences_list_dummy,
        preferences_dummy
):
    preferences = [Preference(**data) for data in preferences_list_dummy]

    assert preferences == preferences_dummy


def test_indifferences(
        indifferences_list_dummy,
        indifferences_dummy
):
    indifferences = [Indifference(**data) for data in indifferences_list_dummy]

    assert indifferences == indifferences_dummy


def test_criterions(
        criterion_list_dummy,
        criterions_dummy
):
    criterions = [Criterion(**data) for data in criterion_list_dummy]

    assert criterions == criterions_dummy


def test_preference_validation():
    with pytest.raises(ValueError, match="Superior and inferior options must be different."):
        Preference(superior='A', inferior='A')


def test_indifference_validation():
    with pytest.raises(ValueError, match="First and second options must be different."):
        Indifference(equal1='A', equal2='A')


def test_criterion_weight_validation():
    with pytest.raises(ValueError, match="Weight must be between 0 and 1."):
        Criterion(criterion_id='g1', weight=1.01, gain=True)


def test_data_validator_validate_criteria(
        performance_table_list_dummy,
        criterions_dummy
):
    with pytest.raises(ValueError, match="Criterion IDs in the list and the data dictionary do not match."):
        DataValidator.validate_criteria(performance_table_list_dummy, criterions_dummy)


def test_data_validator_validate_performance_table(
        performance_table_list_dummy
):
    with pytest.raises(ValueError, match="Keys inside the inner dictionaries are not consistent."):
        DataValidator.validate_performance_table(performance_table_list_dummy)


def test_data_validator_validate_weights(
        performance_table_list_dummy
):
    with pytest.raises(ValueError, match="The sum of all weights must be 1 or all weights must be equal to 1."):
        DataValidator.validate_weights([
            Criterion(criterion_id='g1', weight=0.99, gain=True),
            Criterion(criterion_id='g2', weight=1, gain=True),
            Criterion(criterion_id='g3', weight=1, gain=True)
        ])