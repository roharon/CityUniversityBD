# Answer 1.

```python
/*
DO NOT USE '/'  in the Function named 'score' (prototype : int score(int) )
*/

def score(int value):
    return value//2

num = int(input())
result = score(num)

print(result)
```





# Answer 2.

```python
# function which return reverse of a string
def reverse(s):
    return s[::-1]
 
def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)
 
    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False
  
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans == 1:
    print("Yes")
else:
    print("No")

```



```python
# function to check string is 
# palindrome or not 
def isPalindrome(str):
 
    # Run loop from 0 to len/2 
    for i in xrange(0, len(str)/2): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
```



```python
# function to check string is 
# palindrome or not
def isPalindrome(s):
     
    # Using predefined function to 
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are 
    # equal or not
    if (s == rev):
        return True
    return False
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
```





----------





# Answer 3.

```python
num = int(input())

print("{} tables\n".format(num))
for i in range(0,9):
    print("{} x {}".format(num, i))
```



