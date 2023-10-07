from pydantic import BaseModel, field_validator


class Preference(BaseModel):
    """
    Pydantic dataclass - Represents a preference between two options.
    Attributes:
        superior (str): The superior option.
        inferior (str): The inferior option.
    """
    superior: str
    inferior: str

    @field_validator("inferior")
    def check_different(cls, inferior, values):
        if "superior" in values.data and inferior == values.data["superior"]:
            raise ValueError("Superior and inferior options must be different.")
        return inferior


class Indifference(BaseModel):
    """
    Pydantic dataclass - Represents an indifference criterion with two equal values.

    Attributes:
        equal1 (str): The first equal value.
        equal2 (str): The second equal value.
    """
    equal1: str
    equal2: str

    @field_validator("equal2")
    def check_different(cls, equal2, values):
        if "equal1" in values.data and equal2 == values.data["equal1"]:
            raise ValueError("First and second options must be different.")
        return equal2


class Criterion(BaseModel):
    """
    Pydantic dataclass - Represents a decision criterion.

    Attributes:
        criterion_id (str): The unique identifier for the criterion.
        weight (float): The weight or importance of the criterion.
        gain (bool): Whether the criterion represents a gain (True) or cost (False).
    """
    criterion_id: str
    weight: float
    gain: bool

    @field_validator("weight")
    def check_weight(cls, weight):
        if weight <= 0 or weight > 1:
            raise ValueError("Weight must be between 0 and 1.")
        return weight


class DataValidator:
    @staticmethod
    def validate_criteria(performance_table, criteria_list):
        """Validate whether Criterion IDs in performance_table and criteria_list match."""
        criteria_ids = {criterion.criterion_id for criterion in criteria_list}
        performance_table_ids = {key for item in performance_table.values() for key in item.keys()}

        if criteria_ids != performance_table_ids:
            raise ValueError("Criterion IDs in the list and the data dictionary do not match.")

    @staticmethod
    def validate_weights(criteria_list):
        """Validate whether Criterion weights sum up to 1 or that all are equal to 1"""
        weights = [criterion.weight for criterion in criteria_list]
        total_weight = sum(weights)

        if not (0.99 <= total_weight <= 1.01) and not all(weight == 1 for weight in weights):
            raise ValueError("The sum of all weights must be 1 or all weights must be equal to 1.")

    @staticmethod
    def validate_performance_table(performance_table):
        """Validate whether performance_table IDs are consistent"""
        keys_list = [set(inner_dict.keys()) for inner_dict in performance_table.values()]
        first_keys = keys_list[0]

        for keys in keys_list[1:]:
            if keys != first_keys:
                raise ValueError("Keys inside the inner dictionaries are not consistent.")
