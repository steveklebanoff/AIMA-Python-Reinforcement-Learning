import logging

from aima.mdp import GridMDP, MDP
from aima.utils import turn_left, turn_right
from random import randint
from time import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(message)s')

def char_to_tuple(direction):
    switch = {
        '>' : (1,0),
        '^' : (0,1),
        '<' : (-1, 0),
        '.' : None
    }
    return switch[direction]

class GridMDP(GridMDP):

    def simulate_move(self, state, action):
        # TODO: get percentages from T
        random_number = randint(0, 100)
        if (random_number >= 0) and (random_number <= 9):
            return self.go(state, turn_right(action))
        elif (random_number >= 10) and (random_number <= 20):
            return self.go(state, turn_left(action))
        else:
            return self.go(state, action)

Fig = {}
Fig[17,1] = GridMDP([[-0.04, -0.04, -0.04, +1],
                     [-0.04, None,  -0.04, -1],
                     [-0.04, -0.04, -0.04, -0.04]], 
                    terminals=[(3, 2), (3, 1)])

class PassiveADPAgent(object):

    def __init__(self, action_mdp, policy):
        self.create_policy_and_states(policy)
        self.mdp = MDP(init=(0, 0),
                       actlist=[(1,0), (0, 1), (-1, 0), (0, -1)],
                       terminals=action_mdp.terminals,
                       gamma = 0.9)
        self.action_mdp = action_mdp
        self.utility = { }
        self.sa_freq = { }
        self.outcome_freq = { }

    def create_policy_and_states(self, policy):
        # Create policy and states
        policy.reverse() ## because we want row 0 on bottom, not on top
        self.rows=len(policy)
        self.cols=len(policy[0])
        self.policy = {}
        self.states = set()
        for x in range(self.cols):
            for y in range(self.rows):
                self.policy[x, y] = policy[y][x]
                
                # States are all non-none values
                if policy[y][x] is not None:
                    self.states.add((x, y))

    def get_move_from_policy(self, state_x, state_y):
        return self.policy[state_x][state_y]
        
    def next_action(self, current_state, current_reward):
        # policy = self.policy computed by constructor
        # MDP = mdp object.
        #          MDP.T  - transistion model (initially empty),
        #          MDP.reward - reward
        #          MDP gamma in initializer
        # utility = dictionary u[(0,0)] = 0.57 etc
        # state action frequencies = sa_freq (dict) initially empty
        # outcome frequenes given state outcome and state-action pairs = outcome_freq  initially empty
        #     dict with key being new state, value being another dict with keys being
        #     state, action pairs and values being that percentage
        # previous state, previous action = s,a
        
        # If we're at a terminal we don't want a next move
        if current_state in self.mdp.terminals:
            return False
        
        # Return the next action that the policy dictates
        return self.policy[current_state]

    
    def execute_trial(self):
        # Start at initial state
        current_state = self.mdp.init
        
        # Keep going until we get to a terminal state
        while True:
            logging.debug('--------------------------')
            
            # Get reward for current state
            current_reward = self.action_mdp.R(current_state)
            
            # Calculate move from current state
            next_action = self.next_action(current_state, current_reward)
            
            logging.debug('Current State: %s ' % str(current_state))
            logging.debug('Current Reward: %s ' % current_reward)
            logging.debug('Next action: %s' % next_action)
            
            if next_action == False:
                # End because next_action told us to
                logging.debug('Next_action returned false, stopping')
                break
            
            # Get new current_state
            current_state = self.action_mdp.simulate_move(current_state, char_to_tuple(next_action))

# Setup values
policy = [['>', '>', '>', '.'],
          ['^', None, '^', '.'],
          ['^', '<', '<', '<']]
agent = PassiveADPAgent(Fig[17,1], policy)

trials = 1
# Execute a bunch of trials
for i in range (0,trials):
    agent.execute_trial()

logging.info('Executed %i trials:' % (trials))
logging.info('Utilities: %s' % (agent.utility))