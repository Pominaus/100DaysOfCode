# this file can be found on pastebin here: https://pastebin.com/KeycpyM1
# Original question if you have treehouse access here: https://teamtreehouse.com/community/i-want-to-expand-my-knowledge
# This is code I came up with replying to a user on tree house, 
# The question/answer follows code if you can't access via link:

"""
Comparing the for loop to iteration for calculating the product of the numbers in an array
June 2017, JM
"""
 
from time import time
from sys import setrecursionlimit
 
 
#Function Declarations:
#------------------------------------------
 
def multiLoop(*args):
    '''
   returns the product of the elements in
   args via iteration.
   Expects all args to by numbers
   '''
    total = 1
    for i in range(len(args)):
        total *= aList[i]
    return total
   
def multiply(*args):
    '''
   returns the product of the elements in
   args via recursion.
   Expects all args to be numbers
   '''
    def recursive_product(nums):
        '''
       Recursively updates the product of the
       array nums, returns if length 1
       '''
        if len(nums) > 1:
            return nums[0] * recursive_product(nums[1:])
        else:
            return nums[0]
    return recursive_product(args)
 
def timer_func(func, arg):
    '''
   wrapper function for timing
   other functions.
   Expects a function and a single arguments
   '''
    start = time()
    func(*arg)
    stop = time()
    return stop - start
   
 
#Increase recursion limit, initiate vars:
#------------------------------------------
 
setrecursionlimit(10003)
aList = list(range(1,9999))
total_loop,total_recursion = 0,0
 
 
#Time each function 5 times, take average:
#------------------------------------------
 
for i in range(5):
    total_loop += timer_func(multiLoop, aList)
    total_recursion += timer_func(multiply, aList)
total_loop /= 5
total_recursion /= 5
 
 
#Console feedback
#------------------------------------------
 
print("Loops took {}, recursion took {}.".format(total_loop, total_recursion))
print("Loops were {} times faster".format(total_recursion, total_loop))



"""
Original Question to be answered:
--------------------------------------------------------------------------------------------------------
I want to expand my knowledge
This code here works yet I didn't use slices like it recomended. 
I want to know how i would use slices so that i have a greater 
understanding of how and why it would work

def multiply(*args):
    base = 1
    for arg in args:
        base = base * arg
    return base
    
    
My Answer:
--------------------------------------------------------------------------------------------------------

Hi there!

So first, I thought I should just say, you probably wouldn't - the way you a re doing it is readable, easy to maintain, doesn't require importing anything for one operation, etc. However, to answer the question, the way to do this with slice, would be by recursion. Basically you take the first element of the array, and then pass the rest of the array back into the function, which again takes the first element of the array, and passes the rest back in, until you have only one element in the array, then each function call returns the value it holds, multiplied by the value returned by function it called:

def multiply(*args):
    def recursive_product(nums):
        if len(nums) > 1:
            return nums[0] * recursive_product(nums[1:])
        else:
            return nums[0]
    return recursive_product(args)
Note that the recursive function is inside a wrapper function that appears to do nothing, This has the effect of reducing the args into one single argument so that the len() call works after the first recursion. You could do this by unpacking the list returned by slicing and passing into the next call with recursive_product(*nums[1:]), but no need to do that every single call!

Again, you wouldn't use this in real life, just because 1) You'd hit the recursion limit pretty fast if your had very long lists, and 2) the for loop is much, much faster, while using less memory. When I timed them for 1000 element arrays, recursion was slower by a factor of 3.75 on average. My testing code is here: https://pastebin.com/KeycpyM1

I'd be happy to explain anything if it's not clear, hope it helps :)

"""
