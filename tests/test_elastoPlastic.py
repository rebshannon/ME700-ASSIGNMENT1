import numpy as np
from src.elastoPlasticClassTest import IsotropicHardening as IH
import pytest

@pytest.fixture
def IHModel():
    return IH(E=1000, H = 1000, Y_o = 10)

# def test_update_step_isotropicHardening(IHModel):
#     found = IHModel.get_current_Y()
#     known = 10
#     assert found == known

def test_calc_yield_stress(IHModel):
    found = IHModel.calc_yield_stress()
    known = 10
    assert known == found

def test_phi_trial(IHModel):
    found = IHModel.calc_phi_trial(20,10)
    known = 10
    assert known == found

def test_check_elastic_or_yielding(IHModel):
    founde = IHModel.check_elastic_or_yielding(phi_trial = -2.5,sigma_trial = 7.5)
    knowne = 7.5,0
    foundy = IHModel.check_elastic_or_yielding(phi_trial = 10, sigma_trial = 20)
    knowny = 15,0.005
    assert knowne == founde
    assert knowny == foundy

def test_update_step(IHModel):
    found = IHModel.update_step(delta_epsilon = 0.02)
    known = 10, 15, 0.005
    assert known == found
