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

****longest valid parentheses ********************************************************/
def longestValidParentheses(s):
        stack = []
        lastError = -1
        longestValidParentheses = 0
        for i in range(0, len(s)):
            if s[i] =='(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    lastError = i;
                else:
                    stack.pop()
                    if len(stack)==0:
                        validTill = lastError
                    else:
                         validTill = stack[-1]
                    longestValidParentheses = max(longestValidParentheses, i-validTill)
        return longestValidParenthese

/*************************************************************************/
/**** smallest subarray with a given sum *********************************/

def smallestSubWithSum(arr, n, x): 
  
    # Initilize length of smallest 
    # subarray as n+1 
    min_len = n + 1
  
    # Pick every element as starting point 
    for start in range(0,n): 
      
        # Initialize sum starting  
        # with current start 
        curr_sum = arr[start] 
  
        # If first element itself is greater 
        if (curr_sum > x): 
            return 1
  
        # Try different ending points 
        # for curremt start 
        for end in range(start+1,n): 
          
            # add last element to current sum 
            curr_sum += arr[end] 
  
            # If sum becomes more than x  
            # and length of this subarray 
            # is smaller than current smallest 
            # length, update the smallest  
            # length (or result) 
            if curr_sum > x and (end - start + 1) < min_len: 
                min_len = (end - start + 1) 
          
    return min_len;
/*************************************************************************/

Longest consecutive sequence — should check if end = start + 1 for the comparison arr[end] == (arr[start] + 1)

def longrestconsecutiveseq(arr):
   max_seq = 0
   for start in range(len(arr)):
      seq = 1
      for end in range(start+1,len(arr)):
         if (arr[end] == (arr[start] + 1)) or (arr[end] == prev + 1):
           seq = seq + 1
         else:
           break
   
         if seq > max_seq:
           max_seq = seq 
         prev =  arr[end] 

   return max_seq

/***************************************************************************/
Valid palindrome consider only alpha numeric character 


def palindroine_alpha(str):
   l = [c.lower() for c in str if c.isalnum()]
   return l == l[::-1]
/**********************************************************************************************/
Remove duplicates from a sorted array  in place , juts one value

def removeDuplicates(nums):
        i = 0
        while(i <= len(nums)-2):
            if(nums[i] == nums[i+1]):
                nums.pop(i)
                i -= 1
            i+=1
        return len(nums)

/*****************************************************************************************************/
Remove all occurrences of a number in place in a list

import collections
def removeallinstances(nums,val):
        i = 0
        c = collections.Counter(nums)
        no_val = c[val]
        for i in range(no_val+1):
          if val in nums:
            nums.remove(val)
        return nums  

/*********************************************************************************************************/

Longest substr without repeating characters

def longrestconsecutiveseq(arr):
   max_len = 0
   c = {}
   length = 0
   for i in range(len(arr)):
     if arr[i] not in c:
       c[arr[i]] = 1
       length = length + 1
     else:
       length = 1
       c.clear()
       c[arr[i]] = 1
       #print(c)
       continue
     if length > max_len:
       max_len = length
     #print(i)
     #print(c)    
   return max_len 

/**********************************************************************************/
# Python program to find the longest substring with k unique 
# characters in a given string 
MAX_CHARS = 26
  
# This function calculates number of unique characters 
# using a associative array count[]. Returns true if 
# no. of characters are less than required else returns 
# false. 
def isValid(count, k): 
    val = 0
    for i in xrange(MAX_CHARS): 
        if count[i] > 0: 
            val += 1
  
    # Return true if k is greater than or equal to val 
    return (k >= val) 
  
# Finds the maximum substring with exactly k unique characters 
def kUniques(s, k): 
    u = 0    # number of unique characters 
    n = len(s) 
  
    # Associative array to store the count 
    count = [0] * MAX_CHARS 
  
    # Tranverse the string, fills the associative array 
    # count[] and count number of unique characters 
    for i in xrange(n): 
        if count[ord(s[i])-ord('a')] == 0: 
            u += 1
        count[ord(s[i])-ord('a')] += 1
  
    # If there are not enough unique characters, show 
    # an error message. 
    if u < k: 
        print "Not enough unique characters"
        return
  
    # Otherwise take a window with first element in it. 
    # start and end variables. 
    curr_start = 0
    curr_end = 0
  
    # Also initialize values for result longest window 
    max_window_size = 1
    max_window_start = 0
  
    # Initialize associative array count[] with zero 
    count = [0] * len(count) 
  
    count[ord(s[0])-ord('a')] += 1    # put the first character 
  
    # Start from the second character and add 
    # characters in window according to above 
    # explanation 
    for i in xrange(1,n): 
        # Add the character 's[i]' to current window 
        count[ord(s[i])-ord('a')] += 1
        curr_end+=1
  
        # If there are more than k unique characters in 
        # current window, remove from left side 
        while not isValid(count, k): 
            count[ord(s[curr_start])-ord('a')] -= 1
            curr_start += 1
  
        # Update the max window size if required 
        if curr_end-curr_start+1 > max_window_size: 
            max_window_size = curr_end-curr_start+1
            max_window_start = curr_start 
  
    print "Max substring is : " + s[max_window_start:] \ 
            + " with length " + str(max_window_size
/********************************************************/

Longest common prefix
def longestCommonPrefix(self, strs):

    longest_pre = ""

    if not strs: return longest_pre

    shortest_str = min(strs, key=len)

    for i in range(len(shortest_str)):

        if all([x.startswith(shortest_str[:i+1]) for x in strs]):

            longest_pre = shortest_str[:i+1]

        else:

            break

    return longest_pre

/************************************************************/

Python program to compare two version number 
  
# Method to compare two versions. 
# Return 1 if v2 is smaller, 
# -1 if v1 is smaller,, 
# 0 if equal 
def versionCompare(v1, v2): 
      
    # This will split both the versions by '.' 
    arr1 = v1.split(".") 
    arr2 = v2.split(".") 
  
    # Initializer for the version arrays 
    i = 0 
      
    # We have taken into consideration that both the 
    # versions will contains equal number of delimiters 
    while(i < len(arr1)): 
          
        # Version 2 is greater than version 1 
        if int(arr2[i]) > int(arr1[i]): 
            return -1
          
        # Version 1 is greater than version 2 
        if int(arr1[i]) > int(arr2[i]): 
            return 1
  
        # We can't conclude till now 
        i += 1
          
    # Both the versions are equal 
    return 0


/******************************************************************/


No of words Given , print the number of words in  on a new line ( first word starts with lower case and rest start with uppercase.
For example oneTwoThree . There are  3  words in the string.
 print(1+sum(1 for i in string if i.isupper()))
/**************************************************************************************************/
String password , find missing characters 
def minimumNumber(n, password):
    count = 0    
    if any(i.isdigit() for i in password)==False:
        count+=1
    if any(i.islower() for i in password)==False:
        count+=1
    if any(i.isupper() for i in password)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in password)==False:
        count+=1
    return max(count,6-n)

/**********keep two unique elements******************************************/
from collections import Counter
from itertools import combinations
def is_valid(S):
    c = Counter(S)
    #print c
    if len(c) != 2:
        return False
    for i in xrange(1, len(S)):
        if S[i] == S[i-1]:
            return False
    return True

def keep_letters(lista, keep):
    return filter(lambda x: x in keep, lista)
    
N = int(raw_input())
S = list(raw_input().strip())

letters = {x: 1 for x in S}
letters = list(combinations(letters.keys(), 2))
#print letters
L = list(S)
first = True
m = 0
for keep in letters:
    #print list(S)
    lista = keep_letters(list(S), keep)
    #print lista
    if is_valid(lista):
        m = max(m, len(lista))
    
    
print m
/*************************************************************************************/
Caesar Cipher
https://www.hackerrank.com/challenges/caesar-cipher-1/problem
shifts each letter by a number of letters. 

def main():
      l = input()
      st = input()
      s = int(input())
      l_s = [chr(i) for i in range(ord('a'),ord('z')+1)]
      l_b = [chr(i) for i in range(ord('A'),ord('Z')+1)]
      cpy = ""
      for i in st:
            if i in l_s:
                  cpy += l_s[(l_s.index(i)+s)%26]
            elif i in l_b:
                  cpy += l_b[(l_b.index(i)+s)%26]
            else:
                  cpy += i
      print (cpy)

if __name__ == "__main__":
      main()
           
————————————————————————————————————————————————————————————-----------------------------------------------
. This sentence is known as a pangram because it contains every letter of the alphabet.
def pangrams(str):
  l_a = [chr(i) for i in range(ord('a'), ord('z')+ 1)]   
  new_str = str.lower()
  new_dict = {i:1 for i in str if i in l_a} 
  dict_len = len(new_dict)
  return  dict_len == 26

———————————————————————————————————————————————————————————————————————-------------------------------------
A weighted string is a string of lowercase English letters where each letter has a weight. Character weights are  to  from  to  as shown below:
def weighstr(str):
  dict = {chr(x):ord(chr(x)) - ord('a') + 1  for x in range(ord('a'),ord('z')+1)}
  print(type(dict))

  fin_sum = sum( dict.get(i,0) for i in str)
  return fin_sum

————————————————————————————————————————————--------------------------------------------------------
Alternating Characters
o change it into a string such that there are no matching adjacent characters
t = int(raw_input())
for j in range(t):
	res=0
	str = raw_input()
	if 'A' not in str or 'B' not in str:
		res = len(str)-1
		print res
		continue
	i=0
	while i<(len(str)-1):
		if str[i+1]==str[i]:
			res+=1
		i+=1
	print res
————————————————————————————————————————————————————————————————————————————
Count 010 pattern in a string

def count_pattern(str):

  if '010' not in str:
    return 0
  else:
    return str.count('010')

———————————————————————————————————————————————————————————————————————
/**** string with unique characyters*************/
								 
	def uniquestring(str):
  c = {}
  uniq = 1
  for i in str:
    if i not in c:
       c[i] = 1
    else:
     uniq = 0 
  return uniq == 1    
------------------------------------------------------------------------------------------------------------------
string anagram							 
def anagram(str1,str2):
  a = sorted(str1)
  b = sorted(str2)
  return a == b  
---------------------------------------------------------------------------------------------------------								 
/**** Remove dups from unsorted linked list*********/								 
def removeDuplicates(linkedList):
    previousNode = linkedList.head
    currentNode = previousNode.nextNode

    #set() is like dictionary in python but without value.
    #it stores unique keys using hashmap
    #so searching takes O(1) time
    keys = set([previousNode.data])

    while currentNode:
        data = currentNode.data

        if data in keys:
            #this is duplicate node, so discard it
            previousNode.nextNode = currentNode.nextNode
            currentNode = currentNode.nextNode
        else:
            #put the node data in keys set and move forword
            keys.add(data)
            previousNode = currentNode
            currentNode = currentNode.nextNode

    print "After removing the duplicates:"
    linkedList.printList()
---------------------------------------------------------------------------------------------------------------------

#balanced tree 
								 
https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
								 
------------------------------------------------------------------------------------------------------------------------			 
								 
								 
								 https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/								 
								 
