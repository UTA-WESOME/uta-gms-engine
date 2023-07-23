from xmcda.criteria import Criteria
from xmcda.XMCDA import XMCDA
import numpy as np

import os

from typing import List


class Parser:
    def __init__(self):
        self.xmcda: XMCDA = XMCDA()

    def get_performance_table_array(self, path: str) -> np.ndarray:
        """
        Method responsible for getting performance_table_array

        :param path: Path to XMCDA file

        :return: Array of performances ex. np.ndarray([[26.0, 40.0, 44.0], [2.0, 2.0, 68.0], [18.0, 17.0, 14.0], ...])
        """
        performance_table_list: List[np.array] = []
        xmcda: XMCDA = self.__load_file(path)
        criterias_array: np.array = self.__get_criteria(path)

        for alternative in xmcda.alternatives:
            performance_array = np.array(
                [xmcda.performance_tables[0][alternative][xmcda.criteria[i]] for i in range(len(criterias_array))])
            performance_table_list.append(performance_array)

        return np.array(performance_table_list)

    def __get_criteria(self, path: str):
        """
        Private method responsible for getting array of criterias

        :param path: Path to XMCDA file

        :return: Array of criteria ex. np.array(['g1', 'g2', 'g3'])
        """
        criteria_array: List = []
        xmcda: XMCDA = self.__load_file(path)
        criteria_xmcda: Criteria = xmcda.criteria

        for criteria in criteria_xmcda:
            criteria_array.append(criteria.id)

        return np.array(criteria_array)

    def __load_file(self, path: str) -> XMCDA:
        """
        Private method responsible for loading XMCDA files from tests/files location.
        To be refined later when we will read files from different location

        :param path: Path to XMCDA file

        :return: XMCDA
        """
        current_script_path: str = os.path.dirname(os.path.abspath(__file__))
        directory_path: str = os.path.dirname(os.path.dirname(current_script_path))
        refined_path: str = os.path.normpath(os.path.join(directory_path, f"./tests/files/{path}"))

        xmcda: XMCDA = self.xmcda.load(refined_path)

        return xmcda
