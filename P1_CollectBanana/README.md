### Project 1 Navigation Collect Banana

#### Introduction
The project is to collect banana in a 3D unity environment.

##### State space
There is a total of 37 parameters defining the state spaces, including the velocity of the agent and ray-based perception of objects around agent's forward direction. It is a continuous state space, hence we need to use a Neural Network to approximate the state space value.

Below is a video illustration of the Banana Collectors Environment
[Banana Collectors](https://youtu.be/heVMs3t9qSk)

##### Action space
There is a total of 4 actions - 
    - walk forward  : 0
    - walk backward : 1
    - turn left     : 2
    - turn right    : 3

##### Rewards
In this project, the agent need to collect a rewards of more than 13 to consider the task is solved (13 bananas!)
a reward of +1 is associated with every yellow banana collected, while a reward of -1 is given for any purple banana.

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
1. Checkpoint.pth is the saved weight from the training
