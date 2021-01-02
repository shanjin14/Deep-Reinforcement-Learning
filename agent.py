import numpy as np
from collections import defaultdict
import random

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.alpha = 0.5 # 50% of the recent value are accounted
        self.eps = 0.3 # bigger eps mean more chance to do random action to explore 
        self.gamma = 0.65 #future value is discounted by 0.9

    def update_Q_expsarsa(self, alpha, gamma, nA, eps, Q, state, action, reward, next_state=None):
        """Returns updated Q-value for the most recent experience."""
        current = Q[state][action]         # estimate in Q-table (for current state, action pair)
        policy_s = np.ones(nA) * eps / nA  # current policy (for next state S')
        policy_s[np.argmax(Q[next_state])] = 1 - eps + (eps / nA) # greedy action
        Qsa_next = np.dot(Q[next_state], policy_s)         # get value of state at next time step
        target = reward + (gamma * Qsa_next)               # construct target
        new_value = current + (alpha * (target - current)) # get updated value 
        return new_value
    
    def epsilon_greedy(self, Q, state, nA, eps):
        """Selects epsilon-greedy action for supplied state.
    
        Params
        ======
        Q (dictionary): action-value function
        state (int): current state
        nA (int): number actions in the environment
        eps (float): epsilon
        """
        if random.random() > eps: # select greedy action with probability epsilon
            return np.argmax(Q[state])
        else:                     # otherwise, select an action randomly one out of the 6 actions
            return random.choice(np.arange(self.nA))        
        
        
    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        action = self.epsilon_greedy(self.Q, state, self.nA, self.eps)  
        #print("selected action: {} given state: {}.".format(action,state))
        return action

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        self.Q[state][action] = self.update_Q_expsarsa(self.alpha, self.gamma, self.nA, self.eps, self.Q, \
                                                 state, action, reward, next_state)      
        
        if done:
            self.eps /= 1.55
        
        
        
