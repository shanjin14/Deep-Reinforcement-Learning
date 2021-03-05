## Project 1 - Navigation 

### Learning Algorithm
The learning algorithm used in this project is double DQN with experience replay. 

#### double DQN
Deep Q Network is similar to the tabular method of Q Learning. The main difference is that we are dealing with a continuous state space while we are dealing with dsicrete space in Q Learning which we ca tabulate all possible state-action pair value in tabular form in a small discrete state space.

To deal with large continuous space, we used a Neural Network as Function Approximator so that we can work on a continuous space. 

#### TD update
Instead of updating the value itself in a tabular method like Q Learning, we will be updating the weight of the Deep Neural Network using the TD error.

![Weight Update Using TD Error](https://cdn-media-1.freecodecamp.org/images/1*Zplt-1wTWu_7BGmZCBFjbQ.png)

Reference: https://www.freecodecamp.org/news/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682/

As we can see from the above formula we use the max Q value in the next state as the target and compute the TD error and then use it to weight gradient for each weight.


##### Why double?
As we are not using the actual reward to update the weight like we normally did in deep learning, hence the error can be compounded and like to divergence instead of convergence and hence over-estimated the Q value.
To overcome this, the research showed that we can maintain two network --local the actual one we will be using,  a target network that used for calculate TD target. 
The target network stay stationary for a while as the target and then use it to get the TD target (The part with max operator) and then we update the target network once in a while to change our target network
In the implementation, the target network is only updated once every four step in an episode.

Research paper as below:
[Link](https://arxiv.org/abs/1509.06461)


##### Neural Network for State Value Function Approximation
The input of the neural network (the "x") is 37 states. The output of the neural network (the "y") is the value of each action (a total of 4 action for each state)
In summary, we take the input of each state and provide an estimated Q value for each action (Q(s,a) just like Q learning/SARSA)
TL;DR - we have 37 state as "x" and 4 Q value as "y"

###### The model architecture
Input layer      (37 weights): 37 inputs
1st hidden layer (64 weights): 37 inputs --> 64 outputs  . apply ReLU(Rectified Linear Unit) activation fucntion on the 1st hidden layer output

2nd hidden layer (64 weights): 64 inputs --> 64 outputs .  apply ReLU(Rectified Linear Unit) activation fucntion on the 2nd hidden layer output
output layer     (4 weights) : 64 output --> 4 weights 


##### Why experience replay?
The data we collected for training in each epsisode is correlated. They are not i.i.d (indepdent and identically distributed) that we normally used in Machine Learning model.
Without experience replay, the weight after in each episode will overfitted in the nearby region explored by the Agent in that episode.

Experience replay is to store all the collected (S,A,R,S') into a bucket and we randomly sample a subset of them for doing the trianing. This is to de-correlate the data so that we have the weight udpate that generalise to bigger state space. 

Without experience replay and we can think of an extreme example that the agent decide to stay at 1 state and keep doing 4 actions in one episode. it means the data we have is 1 state (same value for 37 inputs) and varying Q value (as it is estimated by target network that keep revised every 4 steps in one episode). It will then skewed the entire network weights overfitted to the one state and nothing else. 



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
