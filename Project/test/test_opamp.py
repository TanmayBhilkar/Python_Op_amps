from opamp import inv_Opamp
from opamp import n_inv_Opamp
from opamp import diff_Opamp
from opamp import sum_Opamp
from opamp import vol_foll
    
def test_inv_Opamp():
    assert 1.5 == inv_Opamp(1,2,3,4)
    assert 2.666 == inv_Opamp(2,3,4,5)


def test_n_inv_Opamp():
    assert 2.5==n_inv_Opamp(1,2,3,4)
    assert 3.666==n_inv_Opamp(2,3,4,5)

def test_diff_Opamp():
    assert -0.5==diff_Opamp(1,2,3,4)
    assert -0.666==diff_Opamp(2,3,4,5)
    

def test_sum_Opamp():
    assert 3.5==sum_Opamp(1,2,3,4)
    assert 6.0==sum_Opamp(2,3,4,5)  

def test_vol_foll():
    assert 12==vol_foll(3,4)
    assert 6.0==vol_foll(2,3)  

