from xmcda.criteria import Criteria
from xmcda.XMCDA import XMCDA

import os

from typing import List


class Parser:
    def __init__(self):
        self.xmcda: XMCDA = XMCDA()

    def get_performance_table_list(self, path: str) -> List[List]:
        """
        Method responsible for getting list of performances

        :param path: Path to XMCDA file

        :return: List of alternatives ex. [[26.0, 40.0, 44.0], [2.0, 2.0, 68.0], [18.0, 17.0, 14.0], ...]
        """
        performance_table_list: List[List] = []
        xmcda: XMCDA = self._load_file(path)
        criterias_list: List = self._get_criteria(path)

        for alternative in xmcda.alternatives:
            performance_list: List = []
            for i in range(len(criterias_list)):
                performance_list.append(xmcda.performance_tables[0][alternative][xmcda.criteria[i]])
            performance_table_list.append(performance_list)

        return performance_table_list

    def _get_criteria(self, path: str):
        """
        Private method responsible for getting list of criterias

        :param path: Path to XMCDA file

        :return: List of criteria ex. ['g1', 'g2', 'g3']
        """
        criteria_list: List = []
        xmcda: XMCDA = self._load_file(path)
        criteria_xmcda: Criteria = xmcda.criteria

        for criteria in criteria_xmcda:
            criteria_list.append(criteria.id)

        return criteria_list

    def _load_file(self, path: str) -> XMCDA:
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
