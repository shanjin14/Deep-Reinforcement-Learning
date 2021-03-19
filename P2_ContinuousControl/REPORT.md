## Project 2 - Continuous Control 

### Learning Algorithm
The learning algorithm used in this project is DDPG (Deep Deterministic Policy Gradient)

#### DDPG Introduction
DDPG 


##### key changes added to achieve the 30 scores


##### Neural Network for State Value Function Approximation
The input of the neural network (the "x") is 37 states. The output of the neural network (the "y") is the value of each action (a total of 4 action for each state)
In summary, we take the input of each state and provide an estimated Q value for each action (Q(s,a) just like Q learning/SARSA)
TL;DR - we have 37 state as "x" and 4 Q value as "y"

###### The model architecture
Input layer      (37 weights): 37 inputs
1st hidden layer (64 weights): 37 inputs --> 64 outputs  . apply ReLU(Rectified Linear Unit) activation fucntion on the 1st hidden layer output

2nd hidden layer (64 weights): 64 inputs --> 64 outputs .  apply ReLU(Rectified Linear Unit) activation fucntion on the 2nd hidden layer output
output layer     (4 weights) : 64 output --> 4 weights 





#### Hyperparameters 
Parameter used as follows:
1. BUFFER_SIZE = 10,000  # replay buffer size
2. BATCH_SIZE = 64         # minibatch size
3. GAMMA = 0.99            # discount factor
4. TAU = 0.001             # for soft update of target parameters
5. Learning Rate = 0.0005              # learning rate 
6. UPDATE_EVERY = 4        # how often to update the network


### Plots of rewards
![Plotted Rewards](https://github.com/shanjin14/Deep-Reinforcement-Learning/blob/main/P1_CollectBanana/Reward%20Chart.png)

The agent takes only 433 episodes to reach +13 rewards.

### Ideas for Future Work
There are several directions that we can further refine the RL agent performance.
1. neural network architecture - we could refine more hidden layer so that it can approximate the state value better
2. prioritised experience replay - priortised experience replay could help the learning
3. hyperparameter tuning - there are a total 6 hyperparameters in the RL agent. We can see any of the hyperparameters can help the learning


### Reference
1. Most code is referencing the base sample provided by Udacity Deep Reinforcement Learning Github(https://github.com/udacity/deep-reinforcement-learning)
