from typing import Tuple, List, Dict

from pulp import LpVariable, LpProblem, LpMinimize, GLPK, value, LpMaximize, lpSum, LpAffineExpression


class Solver:

    def __init__(self):
        self.name = 'UTA GMS Solver'

    def __str__(self):
        return self.name

    def get_hasse_diagram_dict(
            self,
            performance_table_list: List[List[float]],
            alternatives_id_list: List[str],
            preferences: List[List[int]],
            indifferences: List[List[int]],
            weights: List[float]
    ) -> List[str]:
        """
        Method for getting hasse diagram dict

        :param performance_table_list:
        :param alternatives_id_list:
        :param preferences:
        :param indifferences:
        :param weights:

        :return refined_necessary:
        """

        necessary: List[List[str]] = []
        for i in range(len(performance_table_list)):
            for j in range(len(performance_table_list)):
                if i == j:
                    continue

                problem: LpProblem = self._calculate_epsilon(
                    performance_table_list=performance_table_list,
                    preferences=preferences,
                    indifferences=indifferences,
                    weights=weights,
                    alternative_id_1=i,
                    alternative_id_2=j
                )

                if problem.variables()[0].varValue <= 0:
                    necessary.append([alternatives_id_list[i], alternatives_id_list[j]])

        direct_relations: Dict[str, Dict[str]] = {}

        for relation in necessary:
            node1, node2 = relation
            direct_relations.setdefault(node1, set()).add(node2)

        for node1, related_nodes in direct_relations.items():
            related_nodes_copy: Dict[str] = related_nodes.copy()
            for node2 in related_nodes:
                # Check if node2 is also related to any other node that is related to node1
                for other_node in related_nodes:
                    if other_node != node2 and other_node in direct_relations and node2 in direct_relations[other_node]:
                        # If such a relationship exists, remove the relation between node1 and node2
                        related_nodes_copy.remove(node2)
                        break
            direct_relations[node1]: Dict[str] = related_nodes_copy

        return direct_relations

    def _calculate_epsilon(
            self,
            performance_table_list: List[List[float]],
            preferences: List[List[int]],
            indifferences: List[List[int]],
            weights: List[float],
            alternative_id_1: int = -1,
            alternative_id_2: int = -1
    ) -> LpProblem:
        """
        Main calculation method for problem-solving.
        The idea is that this should be a generic method used across different problems

        :param performance_table_list:
        :param preferences:
        :param indifferences:
        :param weights:
        :param alternative_id_1:
        :param alternative_id_2:

        :return:
        """
        problem: LpProblem = LpProblem("UTA-GMS", LpMaximize)

        epsilon: LpVariable = LpVariable("epsilon")

        u_list, u_list_dict = self._create_variables_list_and_dict(performance_table_list)

        # Normalization constraints
        last_elements: List[LpVariable] = [sublist[-1] for sublist in u_list]
        problem += lpSum(last_elements) == 1

        for i in range(len(u_list)):
            problem += u_list[i][0] == 0

        # Monotonicity constraint
        for i in range(len(u_list)):
            for j in range(1, len(u_list[i])):
                problem += u_list[i][j] >= u_list[i][j - 1]

        # Bounds constraint
        for i in range(len(u_list)):
            for j in range(1, len(u_list[i]) - 1):
                problem += u_list[i][-1] >= u_list[i][j]
                problem += u_list[i][j] >= u_list[i][0]

        # Preference constraint
        for preference in preferences:
            left_alternative: List[float] = performance_table_list[preference[0]]
            right_alternative: List[float] = performance_table_list[preference[1]]

            left_side: List[LpVariable] = []
            right_side: List[LpVariable] = []
            for i in range(len(u_list_dict)):
                left_side.append(u_list_dict[i][left_alternative[i]])
                right_side.append(u_list_dict[i][right_alternative[i]])

            weighted_left_side: List[LpAffineExpression] = []
            weighted_right_side: List[LpAffineExpression] = []
            for u in left_side:
                i: int = int(str(u).split('_')[1])
                weighted_left_side.append(weights[i] * u)

            for u in right_side:
                i: int = int(str(u).split('_')[1])
                weighted_right_side.append(weights[i] * u)

            problem += lpSum(weighted_left_side) >= lpSum(weighted_right_side) + epsilon

        # Indifference constraint
        for indifference in indifferences:
            left_alternative: List[float] = performance_table_list[indifference[0]]
            right_alternative: List[float] = performance_table_list[indifference[1]]

            left_side: List[LpVariable] = []
            right_side: List[LpVariable] = []
            for i in range(len(u_list_dict)):
                left_side.append(u_list_dict[i][left_alternative[i]])
                right_side.append(u_list_dict[i][right_alternative[i]])

            weighted_left_side: List[LpAffineExpression] = []
            weighted_right_side: List[LpAffineExpression] = []
            for u in left_side:
                i: int = int(str(u).split('_')[1])
                weighted_left_side.append(weights[i] * u)

            for u in right_side:
                i: int = int(str(u).split('_')[1])
                weighted_right_side.append(weights[i] * u)

            problem += lpSum(weighted_left_side) == lpSum(weighted_right_side)

        if alternative_id_1 >= 0 and alternative_id_2 >= 0:
            left_alternative: List[float] = performance_table_list[alternative_id_2]
            right_alternative: List[float] = performance_table_list[alternative_id_1]

            left_side: List[LpVariable] = []
            right_side: List[LpVariable] = []
            for i in range(len(u_list_dict)):
                left_side.append(u_list_dict[i][left_alternative[i]])
                right_side.append(u_list_dict[i][right_alternative[i]])

            weighted_left_side: List[LpAffineExpression] = []
            weighted_right_side: List[LpAffineExpression] = []
            for u in left_side:
                i: int = int(str(u).split('_')[1])
                weighted_left_side.append(weights[i] * u)

            for u in right_side:
                i: int = int(str(u).split('_')[1])
                weighted_right_side.append(weights[i] * u)

            problem += lpSum(weighted_left_side) >= lpSum(weighted_right_side) + epsilon

        problem += epsilon

        problem.solve()

        return problem

    @staticmethod
    def _create_variables_list_and_dict(performance_table: List[list]) -> Tuple[List[list], List[dict]]:
        """
        Method responsible for creating a technical list of variables and a technical dict of variables that are used
        for adding constraints to the problem.

        :param performance_table:

        :return: ex. Tuple([[u_0_0.0, u_0_2.0], [u_1_2.0, u_1_9.0]], [{26.0: u_0_26.0, 2.0: u_0_2.0}, {40.0: u_1_40.0, 2.0: u_1_2.0}])
        """
        u_list: List[List[LpVariable]] = []
        u_list_dict: List[Dict[float, LpVariable]] = []

        for i in range(len(performance_table[0])):
            row: List[LpVariable] = []
            row_dict: Dict[float, LpVariable] = {}

            for j in range(len(performance_table)):
                variable_name: str = f"u_{i}_{performance_table[j][i]}"
                variable: LpVariable = LpVariable(variable_name)

                if performance_table[j][i] not in row_dict:
                    row_dict[performance_table[j][i]] = variable

                flag: int = 1
                for var in row:
                    if str(var) == variable_name:
                        flag: int = 0
                if flag:
                    row.append(variable)

            u_list_dict.append(row_dict)

            row: List[LpVariable] = sorted(row, key=lambda var: float(var.name.split("_")[-1]))
            u_list.append(row)

        return u_list, u_list_dict
