import numpy as np

from examples.flappy.naive_agent import NaiveAgent
from ple.games.flappybird import FlappyBird
from ple import PLE

NB_FRAMES = 2 * 60 * 30  # 2 minutes at 30 fps
RANDOM_SEED = 24


def load_game(display_screen=False):
    # The game
    game = FlappyBird()
    p = PLE(game, fps=30, display_screen=display_screen)
    return p


def load_agent(game):
    # The agent
    agent = NaiveAgent(actions=game.getActionSet())
    return agent


def play(ple, agent, verbose=False):
    # Re-set the random number generator in order to evaluate each candidate
    # on the SAME environment and facilitate candidate comparisons
    rng = np.random.RandomState(RANDOM_SEED)
    ple.rng = rng
    # ple.game.setRNG sets the pygamewrapper only. It's actually NOT used
    # by the FlappyBird implementation
    ple.game.setRNG(rng)
    # so also reset the underlying game (FlappyBird) rng
    ple.game.rng = rng
    # Some objects keep a reference to the rng. Reset them
    ple.game.backdrop = None
    ple.game.player = None
    ple.game.pipe_group = None

    # re-init the game
    ple.init()

    reward = 0.0
    nb_lives = 10
    total_score = 0
    for life in range(nb_lives):
        result = "Won!"  # Until we die, we win
        current_score = NB_FRAMES  # Until we die, we can score the max score
        for frame in range(NB_FRAMES):
            if ple.game_over():
                result = "Died!"
                current_score = frame + 1  # +1 because frame starts at 0
                break  # You lose
            else:
                # Keep playing
                observations = ple.getGameState()
                action = agent.pick_action(reward, observations)
                reward = ple.act(action)
        # End of episode
        ple.reset_game()
        total_score = total_score + current_score
        if verbose:
            print("{}! Score: {} Total score: {} Remaining lives: {} ".
                  format(result, current_score, total_score, nb_lives - life - 1))
    if verbose:
        print("Game over! Your score: {}".format(total_score))
    return total_score


def run():
    game = load_game(display_screen=True)
    agent = load_agent(game)
    play(game, agent, verbose=True)


if __name__ == '__main__':
    run()
