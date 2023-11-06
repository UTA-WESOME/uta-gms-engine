import pytest
from xmcda.XMCDA import XMCDA
from src.utagmsengine.utils.parser_utils import ParserUtils
import sys
import os

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_dir)


def test_load_file():

    xmcda: XMCDA = ParserUtils.load_file('performance_table.xml')

    assert xmcda.alternatives[0].id == 'A'
    assert xmcda.alternatives[5].id == 'F'
    assert xmcda.criteria[0].id == 'g1'
