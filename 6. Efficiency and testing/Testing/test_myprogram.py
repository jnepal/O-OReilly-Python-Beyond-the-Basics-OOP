import pytest
import myprogram

'''
 Run from terminal using command py.test
'''

def test_doubleit():
    assert myprogram.doubleit(10) == 20

def test_doubleit_type():
    with pytest.raises(TypeError):
        myprogram.doubleit('String')