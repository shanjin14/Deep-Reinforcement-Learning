# Deep-Reinforcement-Learning

## Overview
The repo is a collection of (toy) learning example I had went through when doing Deep Reinforcement Learning Nanodegree from Udacity and my Master of Computer Science in Georgia Tech.



### 1. Taxi V3 Example (Discrete state space)
A lot of hand-holding code from Udacity which is helpful to get through the mini project exercise and think though the implementation.
THe implementation is expected SARSA + epsilon-greedy policy 

#### Key learning:
1. Hyperparemeters alpha, gamma , epsilon can be tuned to get higher score.
2. important to implement epsilon decay for each time the episode reach the end state. as you want the agent explore more at start, and exploit the learning as much as they can as soon as they have learned many times how to get the job done

#### Interesting highlight:
1. Found this writeup from OpenAI Gym leaderboard, which the author use bayesian optimization to tune the hyperparemeters
