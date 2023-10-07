from typing import List, Dict, Optional

from pulp import LpProblem

from .utils.solver_utils import SolverUtils
from .utils.dataclasses_utils import DataclassesUtils
from src.utagmsengine.dataclasses import Preference, Indifference, Criterion, DataValidator


class Solver:

    def __init__(self, show_logs: Optional[bool] = False):
        self.name = 'UTA GMS Solver'
        self.show_logs = show_logs

    def __str__(self):
        return self.name

    def get_hasse_diagram_dict(
            self,
            performance_table_list: Dict[str, Dict[str, float]],
            preferences: List[Preference],
            indifferences: List[Indifference],
            criterions: List[Criterion],
            number_of_points: Optional[List[int]] = None
    ) -> Dict[str, set]:
        """
        Method for getting hasse diagram dict

        :param performance_table_list:
        :param preferences: List of Preference objects
        :param indifferences: List of Indifference objects
        :param criterions: List of Criterion objects
        :param number_of_points: default None

        :return direct_relations:
        """
        DataValidator.validate_weights(criterions)
        DataValidator.validate_criteria(performance_table_list, criterions)
        DataValidator.validate_performance_table(performance_table_list)

        refined_performance_table_list: List[List[float]] = DataclassesUtils.refine_performance_table_list(
            performance_table_list=performance_table_list
        )

        refined_preferences: List[List[int]] = DataclassesUtils.refine_preferences(
            performance_table_list=performance_table_list,
            preferences=preferences
        )

        refined_indifferences: List[List[int]] = DataclassesUtils.refine_indifferences(
            performance_table_list=performance_table_list,
            indifferences=indifferences
        )

        refined_weights: List[float] = DataclassesUtils.refine_weights(
            criterions=criterions
        )

        refined_gains: List[bool] = DataclassesUtils.refine_gains(
            criterions=criterions
        )

        alternatives_id_list: List[str] = list(performance_table_list.keys())

        if number_of_points is None:
            necessary: List[List[str]] = []
            for i in range(len(refined_performance_table_list)):
                for j in range(len(refined_performance_table_list)):
                    if i == j:
                        continue

                    problem: LpProblem = SolverUtils.calculate_solved_problem(
                        performance_table_list=refined_performance_table_list,
                        preferences=refined_preferences,
                        indifferences=refined_indifferences,
                        weights=refined_weights,
                        criteria=refined_gains,
                        alternative_id_1=i,
                        alternative_id_2=j,
                        show_logs=self.show_logs
                    )

                    if problem.variables()[0].varValue <= 0:
                        necessary.append([alternatives_id_list[i], alternatives_id_list[j]])

            direct_relations: Dict[str, set] = SolverUtils.calculate_direct_relations(necessary)
        else:
            necessary: List[List[str]] = []
            for i in range(len(refined_performance_table_list)):
                for j in range(len(refined_performance_table_list)):
                    if i == j:
                        continue

                    problem: LpProblem = SolverUtils.calculate_solved_problem_with_predefined_number_of_characteristic_points(
                        performance_table_list=refined_performance_table_list,
                        preferences=refined_preferences,
                        indifferences=refined_indifferences,
                        weights=refined_weights,
                        criteria=refined_gains,
                        number_of_points=number_of_points,
                        alternative_id_1=i,
                        alternative_id_2=j,
                        show_logs=self.show_logs
                    )

                    if problem.variables()[0].varValue <= 0:
                        necessary.append([alternatives_id_list[i], alternatives_id_list[j]])

            direct_relations: Dict[str, set] = SolverUtils.calculate_direct_relations(necessary)

        return direct_relations

    def get_ranking_dict(
            self,
            performance_table_list: Dict[str, Dict[str, float]],
            preferences: List[Preference],
            indifferences: List[Indifference],
            criterions: List[Criterion],
            number_of_points: Optional[List[int]] = None
    ) -> Dict[str, float]:
        """
        Method for getting ranking dict

        :param performance_table_list:
        :param preferences: List of Preference objects
        :param indifferences: List of Indifference objects
        :param criterions: List of Criterion objects
        :param number_of_points: default None

        :return alternatives_and_utilities_dict:
        """
        DataValidator.validate_weights(criterions)
        DataValidator.validate_criteria(performance_table_list, criterions)
        DataValidator.validate_performance_table(performance_table_list)

        refined_performance_table_list: List[List[float]] = DataclassesUtils.refine_performance_table_list(
            performance_table_list=performance_table_list
        )

        refined_preferences: List[List[int]] = DataclassesUtils.refine_preferences(
            performance_table_list=performance_table_list,
            preferences=preferences
        )

        refined_indifferences: List[List[int]] = DataclassesUtils.refine_indifferences(
            performance_table_list=performance_table_list,
            indifferences=indifferences
        )

        refined_weights: List[float] = DataclassesUtils.refine_weights(
            criterions=criterions
        )

        refined_gains: List[bool] = DataclassesUtils.refine_gains(
            criterions=criterions
        )

        alternatives_id_list: List[str] = list(performance_table_list.keys())

        if number_of_points is None:
            problem: LpProblem = SolverUtils.calculate_solved_problem(
                performance_table_list=refined_performance_table_list,
                preferences=refined_preferences,
                indifferences=refined_indifferences,
                weights=refined_weights,
                criteria=refined_gains,
                show_logs=self.show_logs
            )

            variables_and_values_dict: Dict[str, float] = {variable.name: variable.varValue for variable in problem.variables()}

            alternatives_and_utilities_dict: Dict[str, float] = SolverUtils.get_alternatives_and_utilities_dict(
                variables_and_values_dict=variables_and_values_dict,
                performance_table_list=refined_performance_table_list,
                alternatives_id_list=alternatives_id_list,
                weights=refined_weights
            )
        else:
            problem: LpProblem = SolverUtils.calculate_solved_problem_with_predefined_number_of_characteristic_points(
                performance_table_list=refined_performance_table_list,
                preferences=refined_preferences,
                indifferences=refined_indifferences,
                weights=refined_weights,
                criteria=refined_gains,
                number_of_points=number_of_points,
                show_logs=self.show_logs
            )

            variables_and_values_dict: Dict[str, float] = {variable.name: variable.varValue for variable in problem.variables()}

            u_list, u_list_dict = SolverUtils.create_variables_list_and_dict(refined_performance_table_list)

            characteristic_points: List[List[float]] = SolverUtils.calculate_characteristic_points(
                number_of_points, refined_performance_table_list, u_list_dict
            )

            alternatives_and_utilities_dict: Dict[str, float] = SolverUtils.get_alternatives_and_utilities_using_interpolation_dict(
                variables_and_values_dict=variables_and_values_dict,
                performance_table_list=refined_performance_table_list,
                weights=refined_weights,
                characteristic_points=characteristic_points,
                alternatives_id_list=alternatives_id_list,
            )

        return alternatives_and_utilities_dict
