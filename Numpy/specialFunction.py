# zeros
import numpy as np
#1 zeros function
zeros=np.zeros((3,4))
#print("zeros :", zeros)

#2 ones function
ones=np.ones((3,3))
#print("ones : ", ones.astype(int))  # default float converting into int ones.astype(int)

#3 Empty 
#  np.empty() does not initialize the array values. 
# It simply allocates memory and returns whatever data already exists in that memory location.
empty=np.empty((3,3))
#print("empty :", empty) 

# eye method

eye=np.eye((3))
print("eye", eye)

