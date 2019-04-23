import neat
import os
import pickle
from ple.games.flappybird import FlappyBird
from ple import PLE
import time

from examples.flappy.neat_agent import NeatAgent
from examples.flappy.play import play

train_timestamp = time.strftime("%Y%m%d-%H%M%S")
NB_GENERATIONS = 1000


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
    winner = population.run(eval_candidates, n=NB_GENERATIONS)
    print("Best genome's fitness: {}".format(winner.fitness))
    # pickle.dump(winner, open('winner.pkl', 'wb'))


def eval_candidates(candidates, config):
    top_score = 0
    top_candidate = None
    for candidate in candidates:
        game = FlappyBird()
        p = PLE(game, fps=30, display_screen=False)
        candidate_id = candidate[0]
        genome = candidate[1]
        agent = NeatAgent(genome, config, actions=p.getActionSet())
        score = play(p, agent, verbose=False)
        print("Id: {} Fitness: {}".format(candidate_id, score))
        genome.fitness = score
        if score > top_score:
            top_score = score
            top_candidate = candidate
    # Done with evaluation
    # Persist best candidate. Note: train_timestamps is global
    persist_candidate(top_candidate, train_timestamp)


def persist_candidate(candidate, timestamp):
    cid = candidate[0]
    genome = candidate[1]
    score = genome.fitness

    # File name
    persistence_dir = "trained_agents"
    dir_name = os.path.join(persistence_dir, timestamp)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    filename = str(cid) + "_" + str(score) + ".pkl"
    filename = os.path.join(dir_name, filename)

    # Save the file
    pickle.dump(genome, open(filename, 'wb'))
    print("Saved best candidate to {}".format(filename))


if __name__ == '__main__':
    train()
