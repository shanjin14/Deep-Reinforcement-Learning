### Project 2 Continuous Control 

#### Introduction
The project is to control the robotic arm to reach the target location in a 3D unity environment.

##### State space
There is a total of 33 parameters defining the state spaces,
It is a continuous state space, hence we need to use a Neural Network to approximate the state space value.

Below is a video illustration of the Banana Collectors Environment
[Continous Control](https://youtu.be/z4EDWYI723w)

We will be solving the 1 reacher environment.

##### Action space
THe action space is also continuous. There are total 4 parameters define the action space representing the torque input value of the 2 joints

##### Algorithm
Given it's continuous state space and continous action space, we will be using DDPG algorithm in this project


##### Rewards
In this project, the agent need to collect a rewards of more than 30 to consider the task is solved.
A reward of +0.1 is provided for each step that the agent's hand is in the goal location.

#### Instructions
1. Download the environment from here
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
 
2. Run the navigation.ipynb to train the RL agent

#### Dependencies
For more details on the setup of the python environment, we can refer to this page
[Link](https://github.com/udacity/deep-reinforcement-learning#dependencies)



#### Additional notes
1. Checkpoint_actor.pth and Checkpoint_critic.pth are the saved weight from the training
