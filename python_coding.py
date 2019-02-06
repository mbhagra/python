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




