import numpy as np

class PolicyParser:
  def __init__(self, dimensions):
    self.state_count = dimensions['state_count']
    self.action_count = dimensions['action_count']

  def policy(self, P, rewards):
   # print('COMPUTING POLICY')

    best_policy = np.zeros(self.state_count)
    state_values = np.zeros(self.state_count)

    GAMMA = 0.9
    ITERATIONS = 700
    for i in range(ITERATIONS):
      print ("iteration: {0} / {1}".format(i + 1, ITERATIONS))

      for state in range(0, self.state_count):
        state_value = -float('Inf')
    

        for action in range(0, self.action_count):
          action_value = 0

          for state_ in range(0, self.state_count):
           
            action_value += (P[state][action][state_] * state_values[state_] * GAMMA)
            
          if (action_value >= state_value):
            state_value = action_value
            best_policy[state] = action
            
          #for state_ in range(0, self.state_count):
          #  print ("--------------------------- ")
          #  print("transition probability fom state: " + str(state) + " to state': " + str(state_) + " with action: " + str(action) + " is: " + str(P[state][action][state_]))
          #  print("For state value de state: " + str(state)+" the state value of state': " + str(state_) + " is : " + str(state_values[state_]))
          #  print ("action_value: "+ str(action_value))
          #  print ("rewards of state: " + str(state) + " is: "+ str(rewards[state]))
            
            

        #state_values[state] = 0.1*(rewards[state] + state_value)
        state_values[state] = (rewards[state] + state_value)
        #print state_value[state];
        #for state_ in range(0, self.state_count):
          #  print("For state value de state: " + str(state)+" the state value of state': " + str(state_) + " is : " + str(state_values[state_]))
            #print ("--------------------------- ")


    return best_policy
    
    #value_iteration
    #For each state initialize V(s)=0
    #Repeat until convergence
    # For each state update V(s)=R(s)+max_a belongs A SUM s' belongs S(P(s,a,s')*V(s'))
    #Policy in state s is the action a that maximezes V(s)