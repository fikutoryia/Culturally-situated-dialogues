#!/usr/bin/env python

state1=[]
with open ( 'smallmatrix2.txt' , 'r') as filestream:
    #next(filestream)
    for line in filestream:
        currentline=line.split(",")
        state1.append(currentline[0])
    


action=[]
with open ( 'smallmatrix2.txt' , 'r') as filestream:
  # next(filestream)
   for line in filestream:
    currentline=line.split(",")
    action.append(currentline[1].strip())


state2=[]
with open ( 'smallmatrix2.txt' , 'r') as filestream:
  # next(filestream)
   for line in filestream:
    currentline=line.split(",")
    currentline[2]=currentline[2][:-1]
    state2.append(currentline[2])

    
observations = [
   { 
    'state_transitions': [{ 'state': state1[i], 'action': action[i], 'state_':state2[i] },],
    'reward': 0
    } for i in range(0, len(state1))
]


trap_states = [
     {
    'state_transitions': [
      { 'state': '0011001', 'action': '1', 'state_': '0011001' },
      { 'state': '0011001', 'action': '2', 'state_': '0011001' },
      { 'state': '0011001', 'action': '3', 'state_': '0011001' },
      { 'state': '0011001', 'action': '4', 'state_': '0011001' },
      { 'state': '0011001', 'action': '5', 'state_': '0011001' },
      { 'state': '0011001', 'action': '6', 'state_': '0011001' },
      { 'state': '0011001', 'action': '7', 'state_': '0011001' },
    ],
    'reward': 1
  },
  
  
      {
    'state_transitions': [
      { 'state': '011101', 'action': '1', 'state_': '011101' },
      { 'state': '011101', 'action': '2', 'state_': '011101' },
      { 'state': '011101', 'action': '3', 'state_': '011101' },
      { 'state': '011101', 'action': '4', 'state_': '011101' },
      { 'state': '011101', 'action': '5', 'state_': '011101' },
      { 'state': '011101', 'action': '6', 'state_': '011101' },
      { 'state': '011101', 'action': '7', 'state_': '011101' },
    ],
    'reward': 1
  },
  
  {
    'state_transitions': [
      { 'state': '101011', 'action': '1', 'state_': '101011' },
      { 'state': '101011', 'action': '2', 'state_': '101011' },
      { 'state': '101011', 'action': '3', 'state_': '101011' },
      { 'state': '101011', 'action': '4', 'state_': '101011' },
      { 'state': '101011', 'action': '5', 'state_': '101011' },
      { 'state': '101011', 'action': '6', 'state_': '101011' },
      { 'state': '101011', 'action': '7', 'state_': '101011' },
    ],
    'reward': 1
  },
  
    {
    'state_transitions': [
      { 'state': '101111', 'action': '1', 'state_': '101111' },
      { 'state': '101111', 'action': '2', 'state_': '101111' },
      { 'state': '101111', 'action': '3', 'state_': '101111' },
      { 'state': '101111', 'action': '4', 'state_': '101111' },
      { 'state': '101111', 'action': '5', 'state_': '101111' },
      { 'state': '101111', 'action': '6', 'state_': '101111' },
      { 'state': '101111', 'action': '7', 'state_': '101111' },
    ],
    'reward': 1
  },
  
      {
    'state_transitions': [
      { 'state': '101211', 'action': '1', 'state_': '101211' },
      { 'state': '101211', 'action': '2', 'state_': '101211' },
      { 'state': '101211', 'action': '3', 'state_': '101211' },
      { 'state': '101211', 'action': '4', 'state_': '101211' },
      { 'state': '101211', 'action': '5', 'state_': '101211' },
      { 'state': '101211', 'action': '6', 'state_': '101211' },
      { 'state': '101211', 'action': '7', 'state_': '101211' },
    ],
    'reward': 1
  },
  
        {
    'state_transitions': [
      { 'state': '111011', 'action': '1', 'state_': '111011' },
      { 'state': '111011', 'action': '2', 'state_': '111011' },
      { 'state': '111011', 'action': '3', 'state_': '111011' },
      { 'state': '111011', 'action': '4', 'state_': '111011' },
      { 'state': '111011', 'action': '5', 'state_': '111011' },
      { 'state': '111011', 'action': '6', 'state_': '111011' },
      { 'state': '111011', 'action': '7', 'state_': '111011' },
    ],
    'reward': 1
  },
  
  
    {
    'state_transitions': [
      { 'state': '111211', 'action': '1', 'state_': '111211' },
      { 'state': '111211', 'action': '2', 'state_': '111211' },
      { 'state': '111211', 'action': '3', 'state_': '111211' },
      { 'state': '111211', 'action': '4', 'state_': '111211' },
      { 'state': '111211', 'action': '5', 'state_': '111211' },
      { 'state': '111211', 'action': '6', 'state_': '111211' },
      { 'state': '111211', 'action': '7', 'state_': '111211' },
    ],
    'reward': 1
  },
  
      {
    'state_transitions': [
      { 'state': '111111', 'action': '1', 'state_': '111111' },
      { 'state': '111111', 'action': '2', 'state_': '111111' },
      { 'state': '111111', 'action': '3', 'state_': '111111' },
      { 'state': '111111', 'action': '4', 'state_': '111111' },
      { 'state': '111111', 'action': '5', 'state_': '111111' },
      { 'state': '111111', 'action': '6', 'state_': '111111' },
      { 'state': '111111', 'action': '7', 'state_': '111111' },
    ],
    'reward': 1
  },
  
        {
    'state_transitions': [
      { 'state': '111211', 'action': '1', 'state_': '111211' },
      { 'state': '111211', 'action': '2', 'state_': '111211' },
      { 'state': '111211', 'action': '3', 'state_': '111211' },
      { 'state': '111211', 'action': '4', 'state_': '111211' },
      { 'state': '111211', 'action': '5', 'state_': '111211' },
      { 'state': '111211', 'action': '6', 'state_': '111211' },
      { 'state': '111211', 'action': '7', 'state_': '111211' },
    ],
    'reward': 1
  },
  
          {
    'state_transitions': [
      { 'state': '111211', 'action': '1', 'state_': '111211' },
      { 'state': '111211', 'action': '2', 'state_': '111211' },
      { 'state': '111211', 'action': '3', 'state_': '111211' },
      { 'state': '111211', 'action': '4', 'state_': '111211' },
      { 'state': '111211', 'action': '5', 'state_': '111211' },
      { 'state': '111211', 'action': '6', 'state_': '111211' },
      { 'state': '111211', 'action': '7', 'state_': '111211' },
    ],
    'reward': 1
  },
  
            {
    'state_transitions': [
      { 'state': '111011', 'action': '1', 'state_': '111011' },
      { 'state': '111011', 'action': '2', 'state_': '111011' },
      { 'state': '111011', 'action': '3', 'state_': '111011' },
      { 'state': '111011', 'action': '4', 'state_': '111011' },
      { 'state': '111011', 'action': '5', 'state_': '111011' },
      { 'state': '111011', 'action': '6', 'state_': '111011' },
      { 'state': '111011', 'action': '7', 'state_': '111011' },
    ],
    'reward': 1
  },
  
    {
    'state_transitions': [
      { 'state': '111101', 'action': '1', 'state_': '111101' },
      { 'state': '111101', 'action': '2', 'state_': '111101' },
      { 'state': '111101', 'action': '3', 'state_': '111101' },
      { 'state': '111101', 'action': '4', 'state_': '111101' },
      { 'state': '111101', 'action': '5', 'state_': '111101' },
      { 'state': '111101', 'action': '6', 'state_': '111101' },
      { 'state': '111101', 'action': '7', 'state_': '111101' },
    ],
    'reward': 1
  },
  
     {
    'state_transitions': [
      { 'state': '011001', 'action': '1', 'state_': '011001' },
      { 'state': '011001', 'action': '2', 'state_': '011001' },
      { 'state': '011001', 'action': '3', 'state_': '011001' },
      { 'state': '011001', 'action': '4', 'state_': '011001' },
      { 'state': '011001', 'action': '5', 'state_': '011001' },
      { 'state': '011001', 'action': '6', 'state_': '011001' },
      { 'state': '011001', 'action': '7', 'state_': '011001' },
    ],
    'reward': 1
  },
  
       {
    'state_transitions': [
      { 'state': '011101', 'action': '1', 'state_': '011101' },
      { 'state': '011101', 'action': '2', 'state_': '011101' },
      { 'state': '011101', 'action': '3', 'state_': '011101' },
      { 'state': '011101', 'action': '4', 'state_': '011101' },
      { 'state': '011101', 'action': '5', 'state_': '011101' },
      { 'state': '011101', 'action': '6', 'state_': '011101' },
      { 'state': '011101', 'action': '7', 'state_': '011101' },
    ],
    'reward': 1
  },
  
       {
    'state_transitions': [
      { 'state': '111201', 'action': '1', 'state_': '111201' },
      { 'state': '111201', 'action': '2', 'state_': '111201' },
      { 'state': '111201', 'action': '3', 'state_': '111201' },
      { 'state': '111201', 'action': '4', 'state_': '111201' },
      { 'state': '111201', 'action': '5', 'state_': '111201' },
      { 'state': '111201', 'action': '6', 'state_': '111201' },
      { 'state': '111201', 'action': '7', 'state_': '111201' },
    ],
    'reward': 1
  }


  
]



def reinforcementLearning():
    #print '[%s]' % ', '.join(map(str, observations))   #print the list of observations
    #print '[%s]' % ', '.join(map(str, state1))  # print the list of actions
    #print '[%s]' % ', '.join(map(str, state2))
    from learn import MarkovAgent
    mark = MarkovAgent(observations + trap_states)
    mark.learn()
    policy=mark.policy
    f = open('out.txt', 'w')
    #print >> f, mark.policy  # or f.write('...\n')
    f.close()
    print policy;
    return policy;



reinforcementLearning();






    


    
    
