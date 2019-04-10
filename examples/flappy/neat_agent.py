import neat


class NeatAgent(object):
    """
    A NEAT agent: a feed-forward neural network.
    """

    def __init__(self, genome, config, actions):
        self.genome = genome
        self.neural_network = neat.nn.FeedForwardNetwork.create(genome, config)
        self.actions = actions

    def pick_action(self, reward, obs):
        output = self.neural_network.activate(obs.values())
        # There's only 1 output. If it's below the threshold, flap. Otherwise don't flap.
        if output[0] < 0.5:
            return self.actions[0]
        else:
            return self.actions[1]
