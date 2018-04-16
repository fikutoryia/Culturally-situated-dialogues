state1=[]
with open ( 'matrix.txt' , 'r') as filestream:
   for line in filestream:
    currentline=line.split("-")
    state1.append(currentline[0])


action=[]
with open ( 'matrix.txt' , 'r') as filestream:
   for line in filestream:
    currentline=line.split("-")
    action.append(currentline[1])


state2=[]
with open ( 'matrix.txt' , 'r') as filestream:
   for line in filestream:
    currentline=line.split("-")
    state2.append(currentline[2])


for i in range(0, len(state1)):
  observations = [
       { 
          'state_transitions': [
          { 'state': state1[i], 'action': action[i], 'state_':state2[i] },
        ],
            'reward': 0
        },
        ]

trap_states = [
      {
      'state_transitions': [
      { 'state': 'Knows that user knows concept,Knows user culture,', 'action': 'cultureIdentif', 'state_': 'Knows that user knows concept,Knows user culture,' },
      { 'state': 'Knows that user knows concept,Knows user culture,', 'action': 'conceptIdentif', 'state_': 'Knows that user knows concept,Knows user culture,' },
    ],
    'reward': 1
  },
  
  
      {
      'state_transitions': [
      { 'state': 'Knows that user knows concept,Knows concept,Knows user culture,', 'action': 'cultureIdentif', 'state_': 'Knows that user knows concept,Knows concept,Knows user culture,' },
      { 'state': 'Knows that user knows concept,Knows concept,Knows user culture,', 'action': 'conceptIdentif', 'state_': 'Knows that user knows concept,Knows concept,Knows user culture,' },
    ],
    'reward': 1
  },
]


print '[%s]' % ', '.join(map(str, observations))
print '[%s]' % ', '.join(map(str, trap_states))
   

#def reinforcementLearning():
from learn import MarkovAgent
mark = MarkovAgent(observations + trap_states)
mark.learn()
print(mark.policy)

  #  return;
     
#reinforcementLearning();


#f = open('out.txt', 'w')
#print >> f, mark.policy  # or f.write('...\n')
#f.close()




    


    
    
