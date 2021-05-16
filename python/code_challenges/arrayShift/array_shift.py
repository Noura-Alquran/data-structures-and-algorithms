def findLength(list):
  count = 0
  for i in list:
    count+= 1
  return count

def insertShiftArray(list ,length,value):
  if length%2!=0:
     length+=1
  index=int(length/2)
  list[index:index]=[value]
  return list


print(insertShiftArray([2,4,6,8],findLength([2,4,6,8]),5))
print(insertShiftArray([4,8,15,23,42],findLength([4,8,15,23,42]),16))
