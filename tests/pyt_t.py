# Testing pyt
# SLD, 2023-01-14
#

import sys
sys.path.append("../fakeds")

import pytest
from fakeds import pyt



def test_pyt():
    assert pyt(par=True) == True
    return True

    
e