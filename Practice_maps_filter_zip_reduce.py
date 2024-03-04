# map, filter, reduce, zip
from functools import reduce

mylist= [1,2,3,4,5]
youlist = [10,20,30,50]
thelist= [5,15,25 ]
def multiply_by2(items):
      return items * 2

def only_odd(items):
      return items % 2 != 0

def accumulate (acc, item):
      print(acc, item)
      return acc + item
    
print(list(map(multiply_by2,mylist ))) # Map exemple

print(list(filter(only_odd,mylist ))) # filter exemple

print(list(zip(mylist,youlist, thelist ))) # zip exemple


print(reduce( accumulate, mylist, 5)) # reduce exemple

print(mylist ) # value of mylist
print(youlist ) # value of youlist