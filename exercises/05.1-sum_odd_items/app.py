arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]
#Your code go here:
  
def sumOdds(array):
  sumat=0
  for i in range(len(array)):
    if array[i]%2!=0:
      sumat = sumat + array[i]
  return sumat

print(sumOdds(arr))