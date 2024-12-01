#MY PYTHON PRACTICE

#def function_gradeassigning(Array):
#    Grades = ["","","","","","","","","","","",""]
#    length7 = len(Array)
#    for index in range(length7):
#        if Array[index] > 100:
#            Grades[index] = "kya baat he bc"
#        elif Array[index] >= 90 and Array[index] <= 100:
#            Grades[index] = "A+"
#        elif Array[index] >= 80 and Array[index] <= 90:
#            Grades[index] = "A"
#        elif Array[index] >= 70 and Array[index] <= 80:
#            Grades[index] = "B"
#        elif Array[index] >= 60 and Array[index] <= 70:
#            Grades[index] = "C"
#        elif Array[index] >= 50 and Array[index] <= 60:
#            Grades[index] = "D"      
#        elif Array[index] < 50:
#            Grades[index] = "U"
#    return Grades
    
    
#student_marks = [10,20,30,40,50,60,70,80,90,100,110,120]
#print(function_gradeassigning(student_marks))



#CREATE A LINEAR SEARCH THAT OUTPUTS THE LOCATION IN THE ARRAY WHEN ITEM IS FOUND

#LIST = ["Arthur Morgan","John Snow","Dutch Vanderlind","Micah Bell","Jim Milton","John"]
#searchitem = input("please enter the name you want to search:")
#i = 0
#length = len(LIST)
#for index in range(length):
 #   if searchitem == LIST[index]:
  #      i = index
   #     print("your name was found in this array at:", i)
#   else:print("your name was not found in this array")

#CREATE A BINARY SEARCH ALGORITHM 

#array = [2,3,4,5,6,7,8,9,20]
#max = len(array)

#found = False
#searchfailed = False
#first = 0
#last = max - 1
#zero = 0

#searchitem = int(input("please enter a search item:"))

#while found == False and searchfailed == False:
    #middle = int(first + last /2)
    #if array[middle] == searchitem:
     #   found = True
    #elif first >= last:
     #   searchfailed = True
    #elif array[middle] > searchitem:
   #     last = middle - 1 
  #  else: first = middle + 1
 #   zero = middle
        
#print(found, zero)


#class node():
  #  def __init__(self):
 #       self.data = ""
#        self.nextPointer = 0
        
#linkedlist = [node() for i in range(3)]

#for i in range(9):
#    linkedlist[index].data = input("enter the data:")
#    linkedlist[index].nextPointer = input("enter the next pointer:")

#THIS IS A STACK


#max = 8
#topofstack = -1

#stack = ["" for i in range(max - 1)]

#def function_push(item):
#  global topofstack
#  for i in range(max -1):
#    item = input("please enter a new item:")
#    if topofstack < max - 1:
#      topofstack = topofstack +1
#      stack[topofstack] = item
#  return topofstack , stack[topofstack]
  
#newitem = input("please enter a new item")
#function_push(newitem)
#print(topofstack)

#def function_pop():
  #global topofstack
  #if topofstack > -1:
 #   topofstack = topofstack - 1
    
#function_pop()

#print(topofstack)


#THIS IS A QUEUE
size = 8
headptr = 0
tailptr = -1

Queue = ["" for i in range(size -1)]

def function_enqueue(data):
  global tailptr , size
  
  for i in range(size - 1):
    data = input("please enter new item")
    if tailptr < size - 1:
      tailptr = tailptr + 1
      Queue[tailptr] = data
  return tailptr , Queue[tailptr]

new = input("p")
function_enqueue(new)


def function_dequeue():
  global tailptr , headptr
  if tailptr != -1:
    headptr = headptr + 1
  return headptr

function_dequeue()
print(headptr)