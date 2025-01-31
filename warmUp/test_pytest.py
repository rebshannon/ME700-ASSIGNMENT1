import fnAssignment1 as testFns


def test_A_lessThan_B():
    known = "PASS: A is less than B"
    found = testFns.A_lessThan_B(1,10)
    assert known == found

def test_nIterMaxCheck():
    known = "PASS: nIterMax is positive whole number"
    found = testFns.nIterMaxCheck(10)
    assert known == found


def test_A_B_signCheck():
    known = "PASS: f(A) and f(B) have opposite signs"
    found = testFns.A_B_signCheck(1,-3)
    assert known == found

def test_midpoint_A_B():
    assert testFns.midpoint_A_B(2,4) == 3

def test_checkTol():
    **WORK ON9

def test_reassignC():
    assert testFns.reassignC(10, -10, 5, 0, 5, 3) == (3, 5)
    #                       (fA,  fB, fC, A, B, C)   (A, B)

