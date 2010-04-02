from aima.mdp import GridMDP
from aima.utils import turn_left, turn_right
from random import randint

def direction_to_tuple(direction):
    switch = {
        'right' : (1,0),
        'up' : (0,1),
        'left' : (-1, 0),
        'down' : (0, -1)
    }
    return switch[direction]

class GridMDP(GridMDP):

    def simulate_move(mdp, state, action):
        # TODO: get percentages from T
        random_number = randint(0, 100)
        if (random_number >= 0) and (random_number <= 9):
            return mdp.go(state, turn_right(action))
        elif (random_number >= 10) and (random_number <= 20):
            return mdp.go(state, turn_left(action))
        else:
            return mdp.go(state, action)

Fig = {}
Fig[17,1] = GridMDP([[-0.04, -0.04, -0.04, +1],
                     [-0.04, None,  -0.04, -1],
                     [-0.04, -0.04, -0.04, -0.04]], 
                    terminals=[(3, 2), (3, 1)])


# Setup values
# TODO: find from value iteration
policy = [['>', '>', '>', '.'], ['^', None, '^', '.'], ['^', '>', '^', '<']]
mdp = { }
u = [[None,None,None,None],
     [None,None,None,None],
     [None,None,None,None],
     [None,None,None,None]]
sa_freq = { }
outcome_freq = { }

def passive_adp_agent(current_percept):
    # policy = policy
    # MDP = mdp dict.  mdp['P'], mdp['R'], mdp['Y'] initially empty
    # utility = u (grid) i.e. [0][0] initially empty
    # state action frequencies = sa_freq (grid) i.e. [0][0] initially empty
    # outcome frequenes given state outcome and state-action pairs = outcome_freq  initially empty
    #     dict with key being new state, value being another dict with keys being
    #     state, action pairs and values being that percentage
    # previous state, previous action = s,a
    raise NotImplementedError