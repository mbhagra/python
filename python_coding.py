import sys

b = ["banana" , "apple" , "microsoft"]

temp = b[0]
b[0] = b[2]
b[2] = temp

print(b)

a = []

for i in range(1,100):
	if (i%3 == 0 and i%5 == 0):
		a.append(i) 
print a		

for i in b:
	print i

given_list3 = [7,5,3,-2,-3,-5]
i = 0
sum = 0
print sum

while(len(given_list3) > i):
	if given_list3[i] < 0:
		sum+=given_list3[i]
	i+=1	
print(sum)		

for i in range(0):
	print("range 0")

def rotate_left3(nums):
  first = nums[0]
  for i  in range (1,len(nums)):
    nums[i-1] = nums[i]
  nums[len(nums)-1]  = first
	



We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
Go...Save, Compile, Run (ctrl-enter)

def make_bricks(small, big, goal):
  
  if(goal> big*5+small):
      return False
  elif(goal%5> small): 
      return False
  else:
    return True


# We want make a package of goal kilos of chocolate. We have small bars (1 
# kilo each) and big bars (5 kilos each). Return the number of small bars to 
# use, assuming we always use big bars before small bars. Return -1 if it 
# can't be done.
def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
        
    if remainder <= small:
        return remainder
        
    return -1


/*** Plus 1******/

class Solution(object):
    def plusOne(self, digits):
       if digits[-1] < 9 :
        digits[-1] = digits[-1] + 1
       else:
        if len(digits) == 1:
            digits = [1,0]
        else:
            digits = self.plusOne(digits[:-1]) + [0]
       return digits   

/**********************************************************/
/*****finonacci appt******************/

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
/************************************/

/****power of 2 ***********/	
def is_power(n):
    n = n/2
    if n == 2:
        return True
    elif n > 2:
       return is_power(n)
    else:
        return False

/**** palindrome of  alinked list******/

def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    res = []
    while head is not None:
        res.append(str(head.val)) 
        head = head.next
    return res == res[::-1]

/***** Add Digits   *****/

def digital_root(n):
    x = sum(int(digit) for digit in str(n))
    if x < 10:
        return x
    else:
          return digital_root(x)  

/***** Ugly Numberwhose prime factors only include 2, 3, 5 ******/
def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1

/**** Is power of 3 ******/
def is_power_3(n):
    n = n/3
    if n == 3:
        return True
    elif n > 3:
       return is_power_3(n)
    else:
        return False

/***Reverse vowels in a given string***/

One simple solution is to store all the vowels while scanning the string and placing the vowels in the reverse order in another iteration of string.

# Reverse Vowels of a String
from pythonds.basic.stack import Stack

def reverse_string_vowel(rev_str):
 new_list = []
 new_stack = Stack()

 for i in rev_str:
   if i.lower() in ['a', 'e','i','o','u']:
     new_stack.push(i)

 for i in rev_str:
    
   if i.lower()  in ['a', 'e','i','o','u']:
    new_list.append(new_stack.pop())
   else:
    new_list.append(i)
 new_str = ''.join(new_list)  
 return new_str

/***** intersection of two arrays*****/
# intersection of two arrays

def intersection(num1,num2):
  """
  :type num1:list
  :type num2:list
  :return list
  """
  res = []
  cache = {}

  for x in num1:
    if x  not in cache:
      cache[x] = True

  for x in num2:
    if x in cache:
      res.append(x)
      del cache[x]

  return res

/****Intersection of Two Arrays II *****/
Each element in the result should appear as many times as it shows in both arrays.

from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1, c2 = Counter(nums1), Counter(nums2)
        result = []
        for k1 in c1:
            if k1 in c2:
                rf = min(c1[k1], c2[k1])
                result.extend([k1]*rf)
        return result

/****** find the string difference ******/

def find_difference(str1,str2):
  for i in str2:
    if i in str1:
      continue
    else:
      break
  return i       
       
/***** find the  3rd max integer or if it doesn't exist then the max integer *****/

def max_integer(num):
  num.sort()
  len_nums = len(num)

  if len_nums == 3:
    return num[2]
  else:
    return  num[len_nums-1] 
	
/*****number of segments in a string*****/

def num_of_segments(str1):
  new_list = str1.split(" ")
  return len(new_list)

/****** Fibonnacci numbers *******/

def Fibonacci(n):
  if n == 0:
    return  0
  elif n == 1:
    return 1
  else:
    return   Fibonacci(n-1) +  Fibonacci(n-2) 


/***** K-diff Pairs in an Array*************/



 def findPairs(self, nums, k):
        if k < 0 or len(nums)==0: return 0
        count_dict, count = {}, 0
        
        for num in nums:
            count_dict[num] = count_dict.get(num,0) + 1
						
        for key in count_dict:
            if k:
                if key + k in count_dict: count += 1
            else:
                if count_dict[key] >= 2: count += 1
        return count

/*****palindrome part 2 , by removing one char ******/

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        if not s == s[::-1]:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    str1 = s[:left] + s[left+1:]
                    str2 = s[:right] + s[right+1:]
                    return str1 == str1[::-1] or str2 == str2[::-1]
        else:
            return True

/****************** Missing Number **************************************************/
a=[1,2,3,4,5,7,8,9,10]
n = len(a) + 1
(n*(n+1)/2) - sum(a)

Or n = a[-1]

Explanation:

sum of numbers from 0 to n is given by the formula: expectedSum = n(n+1)/2

The actual sum is found by adding all the elements in the array. In the above code this is performed by using the inbuilt python function sum.

Now, the missing number is expectedSum - actualSum.

/**** Move Zeroes******/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
def move_zeros(n):
  count = n.count(0)
  n = [e for e in n if e not in [0]]
  for i in range(count):
    n.append(0)
  print(n)
/***********************************************************************************************/	
	
268. Missing Number
a=[1,2,3,4,5,7,8,9,10]
n = len(a) + 1
(n*(n+1)/2) - sum(a)

Or n = a[-1]

Explanation:

sum of numbers from 0 to n is given by the formula: expectedSum = n(n+1)/2

The actual sum is found by adding all the elements in the array. In the above code this is performed by using the inbuilt python function sum.

Now, the missing number is expectedSum - actualSum.

/**** Move Zeroes******/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
def move_zeros(n):
  count = n.count(0)
  n = [e for e in n if e not in [0]]
  for i in range(count):
    n.append(0)
  print(n) 

/****************************************************************program creek puzzles*****************************************************/


# Python program to right rotate a list by n 
  
# Returns the rotated list 
def rightRotate(lists, num): 
    output_list = [] 
      
    # Will add values from n to the new list 
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item])
—————————————————————————————————————————————————————————————————
/***** reverse the words in the string ******************/def reversewords(str):
        list = str.split(" ")
        list.reverse()
        new_str = " ".join(list)
        return new_str
/**********************************************************************************/
/*** nth smallest element *****/

def kthSmallest(arr, n, k): 
  
    # Sort the given array  
    arr.sort() 
  
    # Return k'th element in the  
    # sorted array  
    return arr[k-1] 

/**********************************************************************/

/*****merge intervals******************/
    def merge(self, intervals):
        res = []    # result list
         
        if len(intervals)==0:
            return res
         
        #sort list according to the start value    
        intervals.sort(key=lambda x:x.start)
         
        res.append(intervals[0])
         
        #scan the list
        for i in xrange(1,len(intervals)):
            cur = intervals[i]
            pre = res[-1]
            #check if current interval intersects with previous one
            if cur.start <= pre.end:
                res[-1].end = max(pre.end, cur.end) #merge
            else:
                res.append(cur) #insert
                 
        return res

/********************************************************************/
/***Two Sum - Find two numbers such that they add up to a specific target number*******/
def twosum(nums,k):
      diff = 0
      for i in range(len(nums)):
        diff =  k -nums[i]
        if diff in nums:
          break
      print(i)
      print(nums.index(diff)) 


/******************************************************************/

Merge sorted array 

def mergeArrays(arr1, arr2, n1, n2): 
    arr3 = [None] * (n1 + n2) 
    i = 0
    j = 0
    k = 0
  
    # Traverse both array 
    while i < n1 and j < n2: 
      
        # Check if current element  
        # of first array is smaller  
        # than current element of  
        # second array. If yes,  
        # store first array element  
        # and increment first array 
        # index. Otherwise do same  
        # with second array 
        if arr1[i] < arr2[j]: 
            arr3[k] = arr1[i] 
            k = k + 1
            i = i + 1
        else: 
            arr3[k] = arr2[j] 
            k = k + 1
            j = j + 1
      
  
    # Store remaining elements 
    # of first array 
    while i < n1: 
        arr3[k] = arr1[i]; 
        k = k + 1
        i = i + 1
  
    # Store remaining elements  
    # of second array 
    while j < n2: 
        arr3[k] = arr2[j]; 
        k = k + 1
        j = j + 1
    print("Array after merging") 
    for i in range(n1 + n2): 
        print(str(arr3[i]), end = " ") 

/*******************************************************************************************************/

Balanced parenthesis

from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
/******************************************************************************************************/
Multiple balanced parentheses 

   # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
/*********************************************************************************************/
