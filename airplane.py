import numpy as np

A= np.array([
  [0,0,0],
  [np.cos(np.deg2rad(10)),0,np.sin(np.deg2rad(10))],
  [-np.sin(np.deg2rad(10)),0,np.cos(np.deg2rad(10))],
])

B = np.array([[20.3],[0],[3.6]])

print(A@B)


A= np.array([
  [ np.cos(np.deg2rad(-90)+0.1),np.sin(np.deg2rad(-90)+0.1),0],
  [-np.sin(np.deg2rad(-90)+0.1),np.cos(np.deg2rad(-90)+0.1),0],
  [ 0,0,0],
])
print(A)

B = np.array([[np.cos(np.deg2rad(-90)+0.1)],[np.sin(np.deg2rad(-90)+0.1)],[0]])

print(A@B)