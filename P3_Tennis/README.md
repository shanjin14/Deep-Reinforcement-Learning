### Project 3 Tennis

#### Introduction
The project is to control the two tennis player agent to keep the ball bounce over the net towards each other in a 3D unity environment.

##### State space
There is a total of 24 parameters defining the state spaces for each agent, which tells about the velocity and position of the ball and racket
It is a continuous state space, hence we need to use a Neural Network to approximate the state space value.

Below is a video illustration of the tennis environment	
[Tennis Environment](https://youtu.be/7TBdqiHPXRI)


##### Action space
THe action space is also continuous. There are a total of 2 parameters define the action space : move towards or away from the net and jumping

##### Algorithm
Given it's continuous state space and continous action space, we will be using DDPG algorithm in this project.
The key changes vs the P2 Continous Control. Two agents will share the actor network, critic network and replay buffer


##### Rewards
In this project, the agent need to collect a rewards of more than 0.5 to consider the task is solved.
A reward of +0.1 is provided for each step if the agent hits the ball over the net

#### Instructions
1. Download the environment from here
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
 
2. Run the Tennis.ipynb to train the RL agent

#### Dependencies
For more details on the setup of the python environment, we can refer to this page
[Link](https://github.com/udacity/deep-reinforcement-learning#dependencies)



#### Additional notes
1. .pth files are the saved weight from the training
