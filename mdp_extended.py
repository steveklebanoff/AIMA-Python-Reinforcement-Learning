from aima.mdp import GridMDP

def value_iteration(mdp, epsilon=0.001):
    "Solving an MDP by value iteration. [Fig. 17.4]"
    U1 = dict([(s, 0) for s in mdp.states])
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy() 
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        
        # allows for gamma to be 1
        if ((gamma < 1) and (delta < epsilon * (1 - gamma) / gamma)) or \
           ((gamma == 1) and (delta < epsilon)):
            return U

Fig171 = GridMDP([[-0.04, -0.04, -0.04, +1],
                    [-0.04, None,  -0.04, -1],
                    [-0.04, -0.04, -0.04, -0.04]], 
                    terminals=[(3, 2), (3, 1)], gamma = 1)


print value_iteration(Fig171, 0.0000001)
