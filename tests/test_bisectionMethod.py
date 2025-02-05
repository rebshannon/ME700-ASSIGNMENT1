import src.bisectionMethodFns as testFns
import pytest 

def test_A_lessThan_B():
    known = "PASS: A is less than B"
    found = testFns.A_lessThan_B(1,10)
    knownf = "FAIL: A should be less than B, exiting"
    foundf = testFns.A_lessThan_B(10,9)
    assert known == found
    assert knownf == foundf
    
def test_nIterMaxCheck():
    known = "PASS: nIterMax is positive whole number"
    found = testFns.nIterMaxCheck(10)
    knownf = "Exiting"
    foundf = testFns.nIterMaxCheck(-1)
    assert known == found
    assert knownf == foundf


def test_A_B_signCheck():
    known = "PASS: f(A) and f(B) have opposite signs"
    found = testFns.A_B_signCheck(1,-3)
    knownf = "Exiting"
    foundf = testFns.A_B_signCheck(2,2)
    assert known == found

def test_midpoint_A_B():
    assert testFns.midpoint_A_B(2,4) == 3

def test_checkTol():
    with pytest.raises(SystemExit):
        testFns.checkTol(1,2,10,4)
    known = 10
    found = testFns.checkTol(5,2,10,4)
    assert known == found

def test_reassignC():
    assert testFns.reassignC(10, -10, 5, 0, 5, 3) == (3, 5)
    assert testFns.reassignC(10,-10, -5, 0, 5, 3) == (0, 3)
    #                       (fA,  fB, fC, A, B, C)   (A, B)

def test_maxIterReached():
    known = "Exiting"
    found = testFns.maxIterReached(10,10,5)
    assert known == found
