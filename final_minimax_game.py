from games import *


class FinalGame(Game):

    succs = dict(A=dict(a1='B', a2='C', a3='D'),
                 B=dict(b1='E', b2='B2'),
                 C=dict(c1='F', c2='G'),
                 D=dict(d1='H', d2='D2'),
                 E=dict(e1='E1', e2='E2'),
                 F=dict(f1='F1', f2='F2'),
                 G=dict(g1='G1', g2='G2'),
                 H=dict(h1='H1', h2='H2', h3='H3'))
    utils = dict(
        B2=3,
        E1=2,
        E2=1,
        F1=3,
        F2=2,
        G1=1,
        G2=3,
        D2=2,
        H1=1,
        H2=2,
        H3=4)
    initial = 'A'

    def actions(self, state):
        return list(self.succs.get(state, {}).keys())

    def result(self, state, move):
        return self.succs[state][move]

    def utility(self, state, player):
        if player == 'MAX':
            return self.utils[state]
        else:
            return -self.utils[state]

    def terminal_test(self, state):
        return state not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

    def to_move(self, state):
        return 'MIN' if state in 'BCD' else 'MAX'
