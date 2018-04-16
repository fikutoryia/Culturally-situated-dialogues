#!/usr/bin/env python

state1=[]
with open ( 'smallmatrix1.txt' , 'r') as filestream:
    #next(filestream)
    for line in filestream:
        currentline=line.split(",")
        state1.append(currentline[0])
    


action=[]
with open ( 'smallmatrix1.txt' , 'r') as filestream:
  # next(filestream)
   for line in filestream:
    currentline=line.split(",")
    action.append(currentline[1].strip())


state2=[]
with open ( 'smallmatrix1.txt' , 'r') as filestream:
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
      { 'state': '011', 'action': '1', 'state_': '011' },
      { 'state': '011', 'action': '5', 'state_': '011' },
      { 'state': '011', 'action': '7', 'state_': '011' },
    ],
    'reward': 1
  },
  
    {
    'state_transitions': [
      { 'state': '111', 'action': '1', 'state_': '111' },
      { 'state': '111', 'action': '5', 'state_': '111' },
      { 'state': '111', 'action': '7', 'state_': '111' },
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
    print >> f, mark.policy  # or f.write('...\n')
    f.close()
    print policy;
    return policy;



reinforcementLearning();






    


    
    
