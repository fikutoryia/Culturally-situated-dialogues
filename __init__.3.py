#!/usr/bin/env python

state1=[]
with open ( 'matrix2.txt' , 'r') as filestream:
    #next(filestream)
    for line in filestream:
        currentline=line.split(",")
        state1.append(currentline[0])
    


action=[]
with open ( 'matrix2.txt' , 'r') as filestream:
  # next(filestream)
   for line in filestream:
    currentline=line.split(",")
    action.append(currentline[1].strip())


state2=[]
with open ( 'matrix2.txt' , 'r') as filestream:
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
      { 'state': '0111011', 'action': '1', 'state_': '0111011' },
      { 'state': '0111011', 'action': '2', 'state_': '0111011' },
      { 'state': '0111011', 'action': '3', 'state_': '0111011' },
      { 'state': '0111011', 'action': '4', 'state_': '0111011' },
      { 'state': '0111011', 'action': '5', 'state_': '0111011' },
      { 'state': '0111011', 'action': '6', 'state_': '0111011' },
      { 'state': '0111011', 'action': '7', 'state_': '0111011' },
    ],
    'reward': 1
  },
  
  {
    'state_transitions': [
      { 'state': '1010101', 'action': '1', 'state_': '1010101' },
      { 'state': '1010101', 'action': '2', 'state_': '1010101' },
      { 'state': '1010101', 'action': '3', 'state_': '1010101' },
      { 'state': '1010101', 'action': '4', 'state_': '1010101' },
      { 'state': '1010101', 'action': '5', 'state_': '1010101' },
      { 'state': '1010101', 'action': '6', 'state_': '1010101' },
      { 'state': '1010101', 'action': '7', 'state_': '1010101' },
    ],
    'reward': 1
  },
  
    {
    'state_transitions': [
      { 'state': '1011101', 'action': '1', 'state_': '1011101' },
      { 'state': '1011101', 'action': '2', 'state_': '1011101' },
      { 'state': '1011101', 'action': '3', 'state_': '1011101' },
      { 'state': '1011101', 'action': '4', 'state_': '1011101' },
      { 'state': '1011101', 'action': '5', 'state_': '1011101' },
      { 'state': '1011101', 'action': '6', 'state_': '1011101' },
      { 'state': '1011101', 'action': '7', 'state_': '1011101' },
    ],
    'reward': 1
  },
  
      {
    'state_transitions': [
      { 'state': '1012101', 'action': '1', 'state_': '1012101' },
      { 'state': '1012101', 'action': '2', 'state_': '1012101' },
      { 'state': '1012101', 'action': '3', 'state_': '1012101' },
      { 'state': '1012101', 'action': '4', 'state_': '1012101' },
      { 'state': '1012101', 'action': '5', 'state_': '1012101' },
      { 'state': '1012101', 'action': '6', 'state_': '1012101' },
      { 'state': '1012101', 'action': '7', 'state_': '1012101' },
    ],
    'reward': 1
  },
  
        {
    'state_transitions': [
      { 'state': '1110111', 'action': '1', 'state_': '1110111' },
      { 'state': '1110111', 'action': '2', 'state_': '1110111' },
      { 'state': '1110111', 'action': '3', 'state_': '1110111' },
      { 'state': '1110111', 'action': '4', 'state_': '1110111' },
      { 'state': '1110111', 'action': '5', 'state_': '1110111' },
      { 'state': '1110111', 'action': '6', 'state_': '1110111' },
      { 'state': '1110111', 'action': '7', 'state_': '1110111' },
    ],
    'reward': 1
  },
  
          {
    'state_transitions': [
      { 'state': '0112011', 'action': '1', 'state_': '0112011' },
      { 'state': '0112011', 'action': '2', 'state_': '0112011' },
      { 'state': '0112011', 'action': '3', 'state_': '0112011' },
      { 'state': '0112011', 'action': '4', 'state_': '0112011' },
      { 'state': '0112011', 'action': '5', 'state_': '0112011' },
      { 'state': '0112011', 'action': '6', 'state_': '0112011' },
      { 'state': '0112011', 'action': '7', 'state_': '0112011' },
    ],
    'reward': 1
  },
  
    {
    'state_transitions': [
      { 'state': '1112111', 'action': '1', 'state_': '1112111' },
      { 'state': '1112111', 'action': '2', 'state_': '1112111' },
      { 'state': '1112111', 'action': '3', 'state_': '1112111' },
      { 'state': '1112111', 'action': '4', 'state_': '1112111' },
      { 'state': '1112111', 'action': '5', 'state_': '1112111' },
      { 'state': '1112111', 'action': '6', 'state_': '1112111' },
      { 'state': '1112111', 'action': '7', 'state_': '1112111' },
    ],
    'reward': 1
  },
  
      {
    'state_transitions': [
      { 'state': '1111101', 'action': '1', 'state_': '1111101' },
      { 'state': '1111101', 'action': '2', 'state_': '1111101' },
      { 'state': '1111101', 'action': '3', 'state_': '1111101' },
      { 'state': '1111101', 'action': '4', 'state_': '1111101' },
      { 'state': '1111101', 'action': '5', 'state_': '1111101' },
      { 'state': '1111101', 'action': '6', 'state_': '1111101' },
      { 'state': '1111101', 'action': '7', 'state_': '1111101' },
    ],
    'reward': 1
  },
  
        {
    'state_transitions': [
      { 'state': '1112111', 'action': '1', 'state_': '1112111' },
      { 'state': '1112111', 'action': '2', 'state_': '1112111' },
      { 'state': '1112111', 'action': '3', 'state_': '1112111' },
      { 'state': '1112111', 'action': '4', 'state_': '1112111' },
      { 'state': '1112111', 'action': '5', 'state_': '1112111' },
      { 'state': '1112111', 'action': '6', 'state_': '1112111' },
      { 'state': '1112111', 'action': '7', 'state_': '1112111' },
    ],
    'reward': 1
  },
  
          {
    'state_transitions': [
      { 'state': '1112101', 'action': '1', 'state_': '1112101' },
      { 'state': '1112101', 'action': '2', 'state_': '1112101' },
      { 'state': '1112101', 'action': '3', 'state_': '1112101' },
      { 'state': '1112101', 'action': '4', 'state_': '1112101' },
      { 'state': '1112101', 'action': '5', 'state_': '1112101' },
      { 'state': '1112101', 'action': '6', 'state_': '1112101' },
      { 'state': '1112101', 'action': '7', 'state_': '1112101' },
    ],
    'reward': 1
  },
  
            {
    'state_transitions': [
      { 'state': '1110101', 'action': '1', 'state_': '1110101' },
      { 'state': '1110101', 'action': '2', 'state_': '1110101' },
      { 'state': '1110101', 'action': '3', 'state_': '1110101' },
      { 'state': '1110101', 'action': '4', 'state_': '1110101' },
      { 'state': '1110101', 'action': '5', 'state_': '1110101' },
      { 'state': '1110101', 'action': '6', 'state_': '1110101' },
      { 'state': '1110101', 'action': '7', 'state_': '1110101' },
    ],
    'reward': 1
  },
  
    {
    'state_transitions': [
      { 'state': '1111011', 'action': '1', 'state_': '1111011' },
      { 'state': '1111011', 'action': '2', 'state_': '1111011' },
      { 'state': '1111011', 'action': '3', 'state_': '1111011' },
      { 'state': '1111011', 'action': '4', 'state_': '1111011' },
      { 'state': '1111011', 'action': '5', 'state_': '1111011' },
      { 'state': '1111011', 'action': '6', 'state_': '1111011' },
      { 'state': '1111011', 'action': '7', 'state_': '1111011' },
    ],
    'reward': 1
  },
  
     {
    'state_transitions': [
      { 'state': '0110011', 'action': '1', 'state_': '0110011' },
      { 'state': '0110011', 'action': '2', 'state_': '0110011' },
      { 'state': '0110011', 'action': '3', 'state_': '0110011' },
      { 'state': '0110011', 'action': '4', 'state_': '0110011' },
      { 'state': '0110011', 'action': '5', 'state_': '0110011' },
      { 'state': '0110011', 'action': '6', 'state_': '0110011' },
      { 'state': '0110011', 'action': '7', 'state_': '0110011' },
    ],
    'reward': 1
  },
  
       {
    'state_transitions': [
      { 'state': '0111001', 'action': '1', 'state_': '0111001' },
      { 'state': '0111001', 'action': '2', 'state_': '0111001' },
      { 'state': '0111001', 'action': '3', 'state_': '0111001' },
      { 'state': '0111001', 'action': '4', 'state_': '0111001' },
      { 'state': '0111001', 'action': '5', 'state_': '0111001' },
      { 'state': '0111001', 'action': '6', 'state_': '0111001' },
      { 'state': '0111001', 'action': '7', 'state_': '0111001' },
    ],
    'reward': 1
  },
  
       {
    'state_transitions': [
      { 'state': '1112011', 'action': '1', 'state_': '1112011' },
      { 'state': '1112011', 'action': '2', 'state_': '1112011' },
      { 'state': '1112011', 'action': '3', 'state_': '1112011' },
      { 'state': '1112011', 'action': '4', 'state_': '1112011' },
      { 'state': '1112011', 'action': '5', 'state_': '1112011' },
      { 'state': '1112011', 'action': '6', 'state_': '1112011' },
      { 'state': '1112011', 'action': '7', 'state_': '1112011' },
    ],
    'reward': 1
  },
  
  
  
  
     {
    'state_transitions': [
      { 'state': '1111111', 'action': '1', 'state_': '1111111' },
      { 'state': '1111111', 'action': '2', 'state_': '1111111' },
      { 'state': '1111111', 'action': '3', 'state_': '1111111' },
      { 'state': '1111111', 'action': '4', 'state_': '1111111' },
      { 'state': '1111111', 'action': '5', 'state_': '1111111' },
      { 'state': '1111111', 'action': '6', 'state_': '1111111' },
      { 'state': '1111111', 'action': '7', 'state_': '1111111' },
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






    


    
    
