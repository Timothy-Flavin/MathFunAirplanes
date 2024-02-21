import numpy as np

arr = np.array([200,300,400,600,1000])

arr_min_max = (arr-np.min(arr))/(np.max(arr)-np.min(arr))
arr_z = (arr-np.mean(arr))/np.std(arr)
arr_d = arr/1000

print(arr_min_max)
print(arr_z)
print(arr_d)

arr2 = np.array([4,8,9,15,21,21,24,25,26,28,29,34])
w = (np.max(arr2) - np.min(arr2))/3
print(arr2<np.min(arr2)+w)
print(np.logical_and((arr2<=np.min(arr2)+2*w),(arr2>np.min(arr2)+w)))
print(arr2>np.min(arr2)+2*w)
b1 = arr2[arr2<=np.min(arr2)+w]
b2 = arr2[np.logical_and((arr2<=np.min(arr2)+2*w),(arr2>np.min(arr2)+w))]
b3 = arr2[arr2>np.min(arr2)+2*w]

print(w)
print(b1)
print(b2)
print(b3)