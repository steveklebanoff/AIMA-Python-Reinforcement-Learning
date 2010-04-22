from aima.mdp import GridMDP, MDP
from aima.utils import turn_left, turn_right
from random import randint

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
        self.utility = [[None,None,None,None],
                        [None,None,None,None],
                        [None,None,None,None],
                        [None,None,None,None]]
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
        
    def calculate_move(self, current_percept):
        # policy = policy
        # MDP = mdp object.
        #          MDP.T  - transistion model (initially empty),
        #          MDP.reward - reward
        #          MDP gamma in initializer
        # utility = u (grid) i.e. [0][0] initially empty
        # state action frequencies = sa_freq (grid) i.e. [0][0] initially empty
        # outcome frequenes given state outcome and state-action pairs = outcome_freq  initially empty
        #     dict with key being new state, value being another dict with keys being
        #     state, action pairs and values being that percentage
        # previous state, previous action = s,a
        raise NotImplementedError

# Setup values
# TODO: find from value iteration (?)
policy = [['>', '>', '>', '.'],
          ['^', None, '^', '.'],
          ['^', '<', '<', '<']]
agent = PassiveADPAgent(Fig[17,1], policy)
