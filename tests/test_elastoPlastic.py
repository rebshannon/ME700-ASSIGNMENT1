import numpy as np
from elastoPlasticClasses import IsotropicHardening as IH
from elastoPlasticClasses import kinematicHardening as KH
import pytest

@pytest.fixture
def IHModel():
    E = 1000
    E_t = 100
    H = E*E_t/(E-E_t)
    return IH(E=E, H = H, Y_o = 10)

@pytest.fixture
def KHModel():
    E = 1000
    E_t = 100
    H = E*E_t/(E-E_t)
    return KH(E=E, H = H, Y_o = 10)

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

def test_check_elastic_or_yielding_IH(IHModel):
    #founde = IHModel.check_elastic_or_yielding(phi_trial = -2.5,sigma_trial = 7.5)
    #knowne = 7.5#,0
    IHModel.check_elastic_or_yielding(phi_trial = 10, sigma_trial = 20)
    knowny = 11#,0.005
    #assert np.isclose(knowne, founde)
    assert np.isclose(knowny, IHModel.sigma_n)

def test_update_step_IH(IHModel):
    IHModel.update_step(delta_epsilon = 0.02)
    assert np.isclose(IHModel.sigma_n, 11)

def test_run_model(IHModel):
    all_epsilon = np.array([0,0,0.001001001001001001])

    found = IHModel.run_model(all_epsilon)
    known = np.array([0,0,1.0010010010010015])

    assert np.allclose(known, found,atol=1e-15)

def test_init_KH_state(KHModel):
    assert KHModel.E == 1000
    assert KHModel.alpha_n == 0

def test_check_elastic_or_YIELDING_KH(KHModel):
    KHModel.check_elastic_or_yielding(10,20,10,10)
    knowns = np.array([11,1,0.009])
    founds = np.array([KHModel.sigma_n,KHModel.alpha_n,KHModel.epsilon_p_n])
    assert np.allclose(knowns,founds)

def test_check_ELASTIC_or_yielding_KH(KHModel):
    KHModel.check_elastic_or_yielding(-10,20,10,10)
    knowns = np.array([20,10,0])
    founds = np.array([KHModel.sigma_n,KHModel.alpha_n,KHModel.epsilon_p_n])
    assert np.allclose(knowns,founds)

def test_update_step_KH(KHModel):
    KHModel.update_step(0.02)
    knowns = np.array([11,1,0.009])
    founds = np.array([KHModel.sigma_n,KHModel.alpha_n,KHModel.epsilon_p_n])
    assert np.allclose(knowns,founds)

