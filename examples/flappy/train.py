import neat
from ple.games.flappybird import FlappyBird
from ple import PLE

from examples.flappy.neat_agent import NeatAgent
from examples.flappy.play import play


def train():
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        'config'
    )
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    winner = population.run(eval_candidates, n=50)
    print("Best genome's fitness: {}".format(winner.fitness))
    # pickle.dump(winner, open('winner.pkl', 'wb'))


def eval_candidates(candidates, config):
    for candidate in candidates:
        game = FlappyBird()
        p = PLE(game, fps=30, display_screen=False)
        candidate_id = candidate[0]
        genome = candidate[1]
        agent = NeatAgent(genome, config, actions=p.getActionSet())
        score = play(p, agent, verbose=False)
        print("Id: {} Fitness: {}".format(candidate_id, score))
        genome.fitness = score


if __name__ == '__main__':
    train()
