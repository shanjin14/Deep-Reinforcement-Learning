## Project 3 - Tennis 

### Learning Algorithm
The learning algorithm used in this project is DDPG (Deep Deterministic Policy Gradient)
It is used for continuous state space  and continuous action space same as what we have experienced in project 2

#### DDPG Introduction
DDPG map continuous state space to generate policy for continuous action space. In this project it means the torque value of 2 joints (total 4 continuous value in single vector)
The single DDPG description can be found here [DDPG Introduction in Project 2](https://github.com/shanjin14/Deep-Reinforcement-Learning/blob/main/P2_ContinuousControl/REPORT.md)

##### key changes to adapt to two agent scenario
1. shared observation space - each agent has its own observation of 24 parameters. We combine them into a shared observation space of 48 parameters. i.e, each agent can see each other position, racket..etc. 
	Essentially, it become a fully observable MDP problem
2. shared action, critic, replay buffer -- both agent share the same actor network, critic network, and replay buffer. so both agent are training the same brain to act in coordination.
3. Batch Normalization in Action and Critic Network - I started with a 4-layer deep Neural Net. However, the agent does not learn anything. After introducing Batch Normalization, the agent is able to learn the policy. 
Batch Normalization is a technique to normalize the data for each mini batch. It seems to help stablize the learning by reducing the internal covariate shift per the paper[2]
4. State representation - The original state representation has 24 parameter. We added in an additional parameter to flag out which player does this observation come from, where 1 represent player 1, -1 represent player 2




###### The model architecture
Actor neural network:
0. Batch Normalization (state_size = 25) from input layer
1. fully connected layer 1 (state_size, 256) (state_size = 25) , follow by relu
1.1. Batch Normalization layer (256)
2. fully connected layer 2 (256, 128) follow by relu
2.1. Batch Normalization layer (128)
2. fully connected layer 3 (128, 128) follow by relu
2.1. Batch Normalization layer (128)
3. fully connected layer 4 (128, action_size) (action_size = 2) 
4. tanh output layer convert fc3 output between -1 and 1

Critic neural network
0. Batch Normalization (state_size = 25) from input layer
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
![Plotted Rewards](https://github.com/shanjin14/Deep-Reinforcement-Learning/blob/main/P3_Tennis/DDPG_MAVariant.png)

The agent takes only 403 episodes to reach +0.5 rewards.


### Ideas for Future Work
There are several directions that we can further refine the RL agent performance.
1. prioritised experience replay
2. I read a paper on M3DDPG. It would be interesting to see how does it perform vs the current Multi Agent DDPG approach [paper here](https://people.eecs.berkeley.edu/~russell/papers/aaai19-marl.pdf)


### Reference
1. Most code is referencing the base sample provided by Udacity Deep Reinforcement Learning Github(https://github.com/udacity/deep-reinforcement-learning)
2. Sergey Loffe, Christian Szegedy. Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift, 2015 [Link](https://arxiv.org/abs/1502.03167)
