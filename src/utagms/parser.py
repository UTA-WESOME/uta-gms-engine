from xmcda.criteria import Criteria
from xmcda.XMCDA import XMCDA

import os

from typing import List


class Parser:
    def __init__(self):
        self.xmcda: XMCDA = XMCDA()

    def get_alternatives_array(self, path: str) -> List[List]:
        """
        Method responsible for getting array of alternatives

        :param path: Path to XMCDA file

        :return: Array of alternatives ex. [[26.0, 40.0, 44.0], [2.0, 2.0, 68.0], [18.0, 17.0, 14.0], ...]
        """
        alternatives_array: List[List] = []
        xmcda: XMCDA = self.__load_file(path)
        criterias_array: List = self.__get_criteria(path)

        for alternative in xmcda.alternatives:
            alternative_array: List = []
            for i in range(len(criterias_array)):
                alternative_array.append(xmcda.performance_tables[0][alternative][xmcda.criteria[i]])
            alternatives_array.append(alternative_array)

        return alternatives_array

    def __get_criteria(self, path: str):
        """
        Private method responsible for getting array of criterias

        :param path: Path to XMCDA file

        :return: Array of criteria ex. ['g1', 'g2', 'g3']
        """
        criteria_array: List = []
        xmcda: XMCDA = self.__load_file(path)
        criteria_xmcda: Criteria = xmcda.criteria

        for criteria in criteria_xmcda:
            criteria_array.append(criteria.id)

        return criteria_array

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


parser = Parser()

