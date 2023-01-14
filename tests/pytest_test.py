import sys
sys.path.append(r"D:\OneDrive\GitHub\2023-01-15_fakeds\fakeds")

from fakeds.fakeds import pyt


def test_passing():
    assert 42 == 42
    
def test_pyt_passing():
    assert pyt(par=True)==True
    

