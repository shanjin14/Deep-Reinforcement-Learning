## Project 1 - Navigation 

### Learning Algorithm
The learning algorithm used in this project is double DQN with experience replay. 

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

### Ideas for Future Work
There are several directions that we can further refine the RL agent performance.
1. neural network architecture - we could refine more hidden layer so that it can approximate the state value better
2. prioritised experience replay - priortised experience replay could help the learning
3. hyperparameter tuning - there are a total 6 hyperparameters in the RL agent. We can see any of the hyperparameters can help the learning


