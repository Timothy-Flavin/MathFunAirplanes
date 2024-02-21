import numpy as np
import math

Jack =  ["M","Y","N","P","N","N","N"]
Mary =  ["F","Y","N","P","N","P","N"]
        # Numerator
        # _,  0,  0   0   0   1   0  = 1  logical 'xor'
        # Denominator options?
        # _   1   0   1   0   1   0  = 3  logical 'or' so J = 1/3 This one
        # _   1   1   1   1   0   1  = 5  logical '==' so J = 2/5
        # _   2   0   2   0   1   0  = 4  sum of vars  so J = 2/6
        
Jim =   ["M","Y","P","N","N","N","N"]
2 / 4

def torf(char):
  if char in ["Y","P"]:
    return 1
  else:
    return 0
  

def jackard(P1,P2):
  both = 0
  one = 0
  for j in range(len(P1)):
    print(f"j: {j} P1[{j}]: {P1[j]}, P2[{j}]: {P2[j]}")
    if torf(P1[j]) != torf(P2[j]):
      both+=1
      print("both")
    if torf(P1[j]) or torf(P2[j]):
      one+=1#torf(P1[j]) + torf(P2[j])
    print("one")

  print(both/one)
  print("-----------------------")

jackard(Jack,Mary)
jackard(Mary,Jim)
jackard(Jack,Jim)

arr = np.zeros((4,4))

x1 = [[1,3,2,4],
      [2,5,0,5]]

for i in range(4):
  for j in range(4):
    arr[i,j] = (x1[0][i]-x1[0][j])**2 + (x1[1][i]-x1[1][j])**2

print(arr)




arr1 = np.array([5,0,3,0,2,0,0,2,0,0])
arr2 = np.array([3,0,2,0,1,1,0,1,0,1])

def cos_sim(arr1,arr2):
  top = arr1*arr2
  bottom = np.sqrt(np.sum(np.square(arr1)))*np.sqrt(np.sum(np.square(arr2)))
  return np.sum(top)/np.sum(bottom)

print(cos_sim(arr1,arr2))



