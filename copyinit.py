state1=[]
with open ( 'matrix.txt' , 'r') as filestream:
   for line in filestream:
    currentline=line.split(",")
    state1.append(currentline[0]+currentline[1]+currentline[2])


action=[]
with open ( 'matrix.txt' , 'r') as filestream:
   for line in filestream:
    currentline=line.split(",")
    action.append(currentline[3])


state2=[]
with open ( 'matrix.txt' , 'r') as filestream:
   for line in filestream:
    currentline=line.split(",")
    state2.append(currentline[4]+currentline[5]+currentline[6])


stateactionspace=[]
for i in range(0, len(state1)):
  stateactionspace.append('{state :'+state1[i]+', action:'+action[i] +', state_:'+state2[i]+'}') 

  
observations = [
       { 
         'state_transitions': [
           
                stateactionspace,
        ],
      'reward': -1
        },
        ]
print observations

trap_states = [
      {
          'state_transitions': [
      { 'state': ' filled[slot1]confirmed[slot1]34', 'action': 'askASlot', 'state_': ' filled[slot1]confirmed[slot1]34' },
    ],
    'reward': 1
  },
]


from learn import MarkovAgent
mark = MarkovAgent(observations + trap_states)
mark.learn()
print(mark.policy)




    


    
    
