import numpy as np


class NaiveAgent(object):
    """
    This is our naive agent. It picks actions at random!
    """

    def __init__(self, actions):
        self.actions = actions

    def pick_action(self, reward, obs):
        return self.actions[np.random.randint(0, len(self.actions))]
