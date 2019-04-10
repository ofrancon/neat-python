# FlappyBird

[FlappyBird](https://en.wikipedia.org/wiki/Flappy_Bird) is a side-scrolling game where the player controls a bird, 
attempting to fly between
 columns of green pipes without hitting them.

# Setup (macOS)

FlappyBird relies on PyGame. It can be a little challenging to install PyGame on MacOS Mojave. See [this page](https://github.com/pygame/pygame/issues/555) for a description of the issue. The setup instructions below will guide you through the installation process

## Homebrew
Install Homebrew:
```commandline
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
See [Homebrew's main page](https://brew.sh/) for more information.

## Python
Install Python using brew
```commandline
brew unlink python 
brew install --ignore-dependencies https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
brew switch python 3.6.5_1
```

## Virtual env
Create a virtual environment
```commandline
python3 -m venv ./venv
source venv/bin/activate
```

## Dependencies
Install the required dependencies
```commandline
pip install -r requirements.txt
```

PLE has to be installed from the sources:
```commandline
cd ..
git clone https://github.com/ntasfi/PyGame-Learning-Environment.git
cd PyGame-Learning-Environment/
pip install -e .
```

## (Optional) Remove libpng warning

In case you're tired of seeing these logs when playing the game:
```commandline
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
```

Install pngcrush:
```commandline
brew install pngcrush
```
And run it on the FlappyBird png assets:
```commandline
~/workspace/PyGame-Learning-Environment/ple/games/flappybird/assets/> find . -type f -iname '*.png' -exec pngcrush -ow
 -rem allb -reduce {} \;
```

# References
## PLE
[Repo](https://github.com/ntasfi/PyGame-Learning-Environment)

[Docs](https://pygame-learning-environment.readthedocs.io/en/latest/user/home.html)

PyGame Learning Environment (PLE) is a learning environment, mimicking the 
Arcade Learning Environment interface, allowing a quick start to Reinforcement
 Learning in Python. The goal of PLE is allow practitioners to focus design of
 models and experiments instead of environment design.

## Gym PLE
[Repo](https://github.com/lusob/gym-ple)

Gym PLE allows to use PLE as a gym environment

## FlappyBird

For a description of the game state and the actions:

[PLE - Flappy Bird](https://pygame-learning-environment.readthedocs.io/en/latest/user/games/flappybird.html)

[Open AI Gym - Flappy Bird](https://github.com/openai/gym/wiki/Leaderboard#flappybird-v0)
