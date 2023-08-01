from xmcda.criteria import Criteria
from xmcda.XMCDA import XMCDA

from typing import List

from .utils.parser_utils import ParserUtils


class Parser:
    def get_performance_table_list(self, path: str) -> List[List]:
        """
        Method responsible for getting list of performances

        :param path: Path to XMCDA file (performance_table.xml)

        :return: List of alternatives ex. [[26.0, 40.0, 44.0], [2.0, 2.0, 68.0], [18.0, 17.0, 14.0], ...]
        """
        performance_table_list: List[List[float]] = []
        xmcda: XMCDA = ParserUtils.load_file(path)
        criterias_list: List = self.get_criteria(path)

        for alternative in xmcda.alternatives:
            performance_list: List[float] = []
            for i in range(len(criterias_list)):
                performance_list.append(xmcda.performance_tables[0][alternative][xmcda.criteria[i]])
            performance_table_list.append(performance_list)

        return performance_table_list

    @staticmethod
    def get_alternatives_id_list(path: str) -> List[str]:
        """
        Method responsible for getting list of alternatives ids

        :param path: Path to XMCDA file (alternatives.xml)

        :return: List of alternatives ex. ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        """
        alternatives_id_list: List[str] = []
        xmcda: XMCDA = ParserUtils.load_file(path)

        for alternative in xmcda.alternatives:
            alternatives_id_list.append(alternative.id)

        return alternatives_id_list

    @staticmethod
    def get_criteria(path: str):
        """
        Method responsible for getting list of criterias

        :param path: Path to XMCDA file

        :return: List of criteria ex. ['g1', 'g2', 'g3']
        """
        criteria_list: List = []
        xmcda: XMCDA = ParserUtils.load_file(path)
        criteria_xmcda: Criteria = xmcda.criteria

        for criteria in criteria_xmcda:
            criteria_list.append(criteria.id)

        return criteria_list
