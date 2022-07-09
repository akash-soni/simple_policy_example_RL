
import gym
import numpy as np
import time

env = gym.make("CartPole-v1")

Observations = env.reset()
print(Observations)

# simple render for 100 episodes
for _ in range(100):
    env.render()

