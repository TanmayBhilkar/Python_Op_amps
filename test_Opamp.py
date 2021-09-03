"import all the functions from the Opamp Module"


from Opamp import INV
from Opamp import NINV
from Opamp import DIFF
from Opamp import SUMM

"test case for function INV OPAMP"
def test_INV():
    assert 1.5 == INV(1,2,3,4)
    assert 2.666 == INV(2,3,4,5)

"test case for function NINV OPAMP"

def test_NINV():
    assert 2.5==NINV(1,2,3,4)
    assert 3.666==NINV(2,3,4,5)
"test case for function DIFF OPAMP"

def test_DIFF():
    assert -0.5==DIFF(1,2,3,4)
    assert -0.666==DIFF(2,3,4,5)
    
"test case for function SUMM OPAMP"

def test_SUMM():
    assert 3.5==SUMM(1,2,3,4)
    assert 6.0==SUMM(2,3,4,5)

if __name__=="__main__":
    main()  