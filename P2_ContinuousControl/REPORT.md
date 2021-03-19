## Project 2 - Continuous Control 

### Learning Algorithm
The learning algorithm used in this project is DDPG (Deep Deterministic Policy Gradient)
It is used for continuous state space  and continuous action space like the project 2 environment

#### DDPG Introduction
DDPG map continuous state space to generate policy for continuous action space. In this project it means the torque value of 2 joints (total 4 continuous value in single vector)
The design of DDPG consists of 2 sets of neural network
actor neural network: it map state space to action space (33 --> 4 ). We apply tanh to the last layer which generate value between -1 and 1 for 4 values in single vector
critic neural network: it map state-action pair input to Q(s,a) value ( (33 + 4)  --> 1 )

##### The step goes this way:
1. Agent use action neural network to generate an action
2. Agent receive feedback(reward, next_step, done) from the environment
3. add them into replay buffer
4. After the replay buffer has sufficient samples, Agent sample a subset of experience and learn from it by:
  a. Given the next step, update the critic neural network
  b. Generate action based on current state using actor neural network
  c. get Q expected from critic neural network given current state and action from actor neural network
  d. actor loss = - Q expected above (i.e we want to update the weight to maximize the Q expected).A good discussion reference [here] (https://www.quora.com/Why-is-the-loss-for-DDPG-Actor-the-product-of-gradients-of-Q-values-actions)
  e. update the weight of the actor critic network

To stabilise the learning above, we used the same technique we have seen in double dqn -- target network. 
Hence, you will need to have:
1. actor_local  - use in step #1, #4b, #4e(update critic local weight)
2. actor_target - use in step #4a
3. critic_local - use in step #4c
4. critic_target - use in step #4a to calculate Q expected for update critic local



##### key changes added to achieve the 30 scores
In the first implementation, I was not able to achieve 30 scores after more than few hundreds episodes. In fact, the agent does not learn anything.
After going through again the material from DRLND, below are the key changes made that I think that make it work:
1. gradient clipping -- we used gradient norm clipping. which rescale the weight update vector size to 1 to limit the exploding gradient that leads to bad learning
3. instead of update target network every 10 steps, update every 20 steps. it improves the stability of the learning
4. decay of the noise -- noise is added at the start of the learning and gradually reduced (less exploration and more exploitation). It helps the stability of the learning
 


###### The model architecture
Actor neural network:
1. fully connected layer 1 (state_size, 128) (state_size = 33) , follow by relu
2. fully connected layer 2 (128, 128) follow by relu
3. fully connected layer 3 (128, action_size) (action_size = 4) 
4. tanh output layer convert fc3 output between -1 and 1

Critic neural network
1. fully connected layer 1 (state_size, 128) (state_size = 33) , follow by relu
3. fully connected layer 2 (128 + action_size, 128) follow by relu
4. fully connected layer 3 (128, 128) follow by relu
6. fully connected output layer 4 map fc3 output to 1 value (Q(s,a))


#### Hyperparameters 
Parameter used as follows:
BUFFER_SIZE = int(1e5)  # replay buffer size
BATCH_SIZE = 128        # minibatch size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
LR_ACTOR = 1e-3         # learning rate of the actor 
LR_CRITIC = 1e-3        # learning rate of the critic
WEIGHT_DECAY = 0  # L2 weight decay
UPDATE_FREQ = 20       # how often to update the network
EPSILON = 1.0
EPSILON_DECAY = 0.000001


### Plots of rewards
![Plotted Rewards](https://github.com/shanjin14/Deep-Reinforcement-Learning/blob/main/P2_ContinuousControl/ddpg_avg_reward.png)

The agent takes only 169 episodes to reach +30 rewards.

### Ideas for Future Work
There are several directions that we can further refine the RL agent performance.
1. prioritised experience replay
2. D4PG / PPO - which we utilise 20 reacher environment to improve the learning


### Reference
1. Most code is referencing the base sample provided by Udacity Deep Reinforcement Learning Github(https://github.com/udacity/deep-reinforcement-learning)
