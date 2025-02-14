import numpy as np

class ElastoPlastic:
    def __init__(self, E, H, Y_o):
        
        # atttributes of ElastoPlastic case
        self.E = E
        self.H = H
        self.Y_o = Y_o
        
        # starts with no stress or strain
        self.sigma_n = 0
        self.epsilon_p_n = 0
    
    def calc_yield_stress(self):
        Y_n = self.Y_o + self.H * self.epsilon_p_n
        return Y_n

    def run_model(self, epsilon_step):
        stress_list = []
        strain_list = []
        for step, ep_n in enumerate(epsilon_step):

            # find delta ep_n
            if step == 0:
                stress_list.append(self.sigma_n)
                continue

            delta_ep_n = ep_n - epsilon_step[step-1]
            if np.isclose(delta_ep_n,0):
                stress_list.append(self.sigma_n)
                continue

            self.update_step(delta_ep_n)  
            stress_list.append(self.sigma_n)
            strain_list.append(self.epsilon_p_n)
        return stress_list, strain_list
   
class IsotropicHardening(ElastoPlastic):

    def calc_phi_trial(self,sigma_trial,Y_n):
        phi_trial = np.abs(sigma_trial) - Y_n
        return phi_trial

    def check_elastic_or_yielding(self,phi_trial,sigma_trial):
        if phi_trial <= 0: # material is elastic
            self.sigma_n = sigma_trial
            self.epsilon_p_n = self.epsilon_p_n
        else: #material is yielding, return mapping
            delta_epsilon = phi_trial / (self.E + self.H)
            self.sigma_n = sigma_trial - np.sign(sigma_trial) * self.E * delta_epsilon
            self.epsilon_p_n = self.epsilon_p_n + delta_epsilon
        return self.sigma_n, self.epsilon_p_n

    def update_step(self,delta_epsilon):
        #function to update attribute of the class based on input epsilon
     
        # find current yield stress
        Y_n = self.calc_yield_stress()

        # elastic predictor with sigma trial
        delta_Sigma_trial = self.E * delta_epsilon
        sigma_trial = self.sigma_n + delta_Sigma_trial

        # find phi trial and check state
        phi_trial = self.calc_phi_trial(sigma_trial,Y_n)
        self.sigma_n, self.epsilon_p_n = self.check_elastic_or_yielding(phi_trial,sigma_trial)
        
        # update sigma
        #self.sigma_n = sigma_trial - np.sign(sigma_trial) * self.E * delta_epsilon

        return Y_n

class kinemticHardening(ElastoPlastic):

    def __init__(self, E, H, Y_o):
        super().__init__(E, H, Y_o)
        self.alpha_n = 0
    
    def check_elastic_or_yielding(self,phi_trial,sigma_trial,alpha_trial,eta_trial):
        if phi_trial <= 0: # elastic
            self.sigma_n = sigma_trial
            self.alpha_n = alpha_trial
            self.epsilon_p_n = self.epsilon_p_n
        else: # plastic
            delta_epsilon = phi_trial / (self.E + self.H)
            self.sigma_n = sigma_trial - np.sign(eta_trial) * self.E * delta_epsilon
            self.alpha_n = self.alpha_n + np.sign(eta_trial) * self.H * delta_epsilon
            self.epsilon_p_n = self.epsilon_p_n + delta_epsilon

    def update_step(self, delta_epsilon):

        # elastic predictor with sigma trial
        sigma_trial = self.sigma_n + self.E * delta_epsilon
        alpha_trial = self.alpha_n
        eta_trial = sigma_trial - alpha_trial
        phi_trial = np.abs(eta_trial) - self.Y_o

        self.check_elastic_or_yielding(phi_trial,sigma_trial,alpha_trial,eta_trial)
        

