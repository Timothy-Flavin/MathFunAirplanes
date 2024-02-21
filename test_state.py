import numpy as np


class agent():
  def __init__(self, n_agents):
    self.commanded_by = np.random.randint(0,2,n_agents)
    self.commanded = np.random.randint(0,6,n_agents)
    self.command_dir = np.random.random((n_agents,2))


ags = [agent(3),agent(3),agent(3)]
for a in ags:
  print(np.concatenate([np.expand_dims(a.commanded_by,axis=1),
                  np.expand_dims(a.commanded,axis=1),
                  a.command_dir],1))
  
