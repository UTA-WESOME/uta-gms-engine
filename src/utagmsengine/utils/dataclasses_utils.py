from typing import List, Dict


class DataclassesUtils:

    @staticmethod
    def refine_performance_table_dict(
            performance_table_dict: Dict[str, Dict[str, float]]
    ) -> List[List[float]]:
        """
        Convert a dictionary of performance table values into a 2D list of floats.

        :param performance_table_dict:
        :return output_list:
        """
        output_list = []
        for key in performance_table_dict:
            inner_list = list(performance_table_dict[key].values())
            output_list.append(inner_list)

        return output_list

    @staticmethod
    def refine_preferences(
            performance_table_dict: Dict[str, Dict[str, float]],
            preferences
    ) -> List[List[int]]:
        """
        Convert a list of Preferences into a list of indices corresponding to alternatives.

        :param performance_table_dict:
        :param preferences:
        :return output:
        """
        output = []
        keys = list(performance_table_dict.keys())

        for preference in preferences:
            superior_index = keys.index(preference.superior)
            inferior_index = keys.index(preference.inferior)
            output.append([superior_index, inferior_index])

        return output

    @staticmethod
    def refine_indifferences(
            performance_table_dict: Dict[str, Dict[str, float]],
            indifferences
    ) -> List[List[int]]:
        """
        Convert a list of Indifferences into a list of indices corresponding to alternatives.

        :param performance_table_dict:
        :param indifferences:
        :return output:
        """
        output = []
        keys = list(performance_table_dict.keys())

        for indifference in indifferences:
            equal1_index = keys.index(indifference.equal1)
            equal2_index = keys.index(indifference.equal2)
            output.append([equal1_index, equal2_index])

        return output

    @staticmethod
    def refine_weights(
            criterions
    ) -> List[float]:
        """
        Extract weights from a list of Criterion objects.

        :param criterions:

        :return output:
        """
        output = []

        for criterion in criterions:
            output.append(criterion.weight)

        return output

    @staticmethod
    def refine_gains(
            criterions
    ) -> List[bool]:
        """
        Extract gains/costs from a list of Criterion objects.

        :param criterions:

        :return output:
        """
        output = []

        for criterion in criterions:
            output.append(criterion.gain)

        return output
