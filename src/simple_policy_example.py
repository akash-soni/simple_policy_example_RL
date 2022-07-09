
from turtle import done
import gym
import numpy as np
import time
from tqdm import tqdm

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
for episode in range(N_episodes): # Running for 200 episodes and for each episode we have 200 steps/trials 
    rewards = 0
    # CartPosition, CartVelocity, PoleAngle, PoleAngularVelocity
    Observations = env.reset() # the pole will be somewhere in the middle on initial positions
    PoleAngle = Observations[2] 
    for step in tqdm(range(N_steps)): 
        env.render()
        action = basic_policy(PoleAngle) # if the pole is moving to right move to right and if pole is moving to left move to left
        Observations, reward, done, info = env.step(action) # after the movement we will  get the information
        time.sleep(0.001)
        rewards += reward
        if done: #Fallen 
            break
    total_reward.append(rewards)






