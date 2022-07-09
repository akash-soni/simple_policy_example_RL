
from turtle import done
import gym
import numpy as np
import time

env = gym.make("CartPole-v1")

# def basic_policy(PoleAngle):
#     if PoleAngle < 0: #fallling left
#         return 0 # move left
#     else: # Move right
#         return 1
         
# def basic_policy(PoleAngle):
#     if PoleAngle < 0: #fallling left
#         return 0 # move left
#     else: # Move right
#         return 1
         
def basic_policy(PoleAngle):
    if PoleAngle < 0: #fallling left
        return 0 # move left
    return 1

total_reward = list()

N_episodes = 200
N_steps = 200


# simple render for 100 episodes
for episode in range(N_episodes):
    rewards = 0
    # CartPosition, CartVelocity, PoleAngle, PoleAngularVelocity
    Observations = env.reset() # initial positions
    PoleAngle = Observations[2] 
    for step in range(N_steps):
        env.render()
        action = basic_policy(PoleAngle)
        Observations, reward, done, info = env.step(action)
        time.sleep(0.001)
        rewards += reward
        if done: #Fallen
            break
    total_reward.append(rewards)

stats = {
    "mean": np.mean(total_reward)
    "std": np.
}




