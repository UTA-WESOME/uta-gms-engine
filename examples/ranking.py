# This file contains simple example of how to use uta-gms-engine package to make a ranking of variants
from xmcda.XMCDA import XMCDA

x = XMCDA()
x.load(r'../tests/files/value_functions.xml')

print(x)
