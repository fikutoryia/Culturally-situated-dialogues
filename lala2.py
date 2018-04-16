observations = [
       { 
          'state_transitions': [
          { 'state': '000', 'action': 'cultId', 'state_':'100' },
          { 'state': '100', 'action': 'conceptId', 'state_':'110' },
          { 'state': '110', 'action': 'UserConceptId', 'state_':'111' }
        ],
            'reward': 0
        },
        
       
       
       { 
          'state_transitions': [
          { 'state': '000', 'action': 'cultId', 'state_':'000' },
          { 'state': '000', 'action': 'conceptId', 'state_':'010' },
          { 'state': '010', 'action': 'UserConceptId', 'state_':'011' },
        ],
            'reward': 0
        },
        
        { 
          'state_transitions': [
          { 'state': '000', 'action': 'cultId', 'state_':'100' },
          { 'state': '100', 'action': 'UserConceptId', 'state_':'100' },
          { 'state': '100', 'action': 'conceptId', 'state_':'110' },
          { 'state': '100', 'action': 'conceptId', 'state_':'111' },

        ],
            'reward': 0
        },
        { 
          'state_transitions': [
          { 'state': '000', 'action': 'UserConceptId', 'state_':'000' },
          { 'state': '100', 'action': 'UserConceptId', 'state_':'100' },
          { 'state': '100', 'action': 'conceptId', 'state_':'110' },
          { 'state': '100', 'action': 'conceptId', 'state_':'111' },

        ],
            'reward': 0
        }
        
       ] 

trap_states = [
      {
          'state_transitions': [
      { 'state': '011', 'action': 'cultId', 'state_': '011' },
      { 'state': '011', 'action': 'UserConceptId', 'state_': '011' },
      { 'state': '011', 'action': 'conceptId', 'state_': '011' }

    ],
    'reward': 1
  },
  
    {
          'state_transitions': [
      { 'state': '111', 'action': 'cultId', 'state_': '111' },
      { 'state': '111', 'action': 'UserConceptId', 'state_': '111' },
      { 'state': '111', 'action': 'conceptId', 'state_': '111' },

    ],
    'reward': 1
  }
]
print '[%s]' % ', '.join(map(str, observations)) 
from learn import MarkovAgent
mark = MarkovAgent(observations + trap_states)
mark.learn()
print(mark.policy)