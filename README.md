# Deep-Reinforcement-Learning

## Overview
The repo is a collection of (toy) learning example / project I had went through when doing Deep Reinforcement Learning Nanodegree from Udacity and my Master of Computer Science in Georgia Tech.


### 1. Taxi V3 Example (Discrete state space)
A lot of hand-holding code from Udacity which is helpful to get through the mini project exercise and think though the implementation.
THe implementation is expected SARSA + epsilon-greedy policy 

### 2. P1 - Collect Banana (Continuous state space , discrete actions, single agent)
Implemented double DQN to 


### 3. P2 - Continuous Control (Continuous state space , continuous action space, single agent)
Implemented single agent DDPG to control the robotic arm to reach target location

### 4. P3 - Tennis (Continuous state space , continuous action space, multi agent)
Implemented Multi Agent DDPG to coordinate to agent to play tennis with another


#### Key learning:
1. Hyperparemeters alpha, gamma , epsilon can be tuned to get higher score.
2. important to implement epsilon decay for each time the episode reach the end state. as you want the agent explore more at start, and exploit the learning as much as they can as soon as they have learned many times how to get the job done

#### Interesting highlight:
1. Found this writeup from OpenAI Gym leaderboard, which the author use bayesian optimization to tune the hyperparemeters

#### Have gone through a bunch of papers during this time
1. [TD Lambda] (http://incompleteideas.net/papers/sutton-88-with-erratum.pdf)
2. [Correlated-Q] (https://www.aaai.org/Papers/ICML/2003/ICML03-034.pdf)
3. DQN - DeepMind (https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)
4. [Dueling Architecture] (https://arxiv.org/abs/1511.06581)
5. [AlphaGo] (http://airesearch.com/wp-content/uploads/2016/01/deepmind-mastering-go.pdf)
