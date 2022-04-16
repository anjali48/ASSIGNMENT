1.def printPairs(arr, n, sum):
 
    # count = 0
 
    # Consider all possible
    # pairs and check their sums
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep = "")
 
 
# Driver Code
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
printPairs(arr, n, sum)

2.def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


3.def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    if size1 != size2:
        return 0
 
    temp = string1 + string1
 
    
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
 
string1 = "AACD"
string2 = "ACDA"
 
if areRotations(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")



4.NO_OF_CHARS = 256

def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
 

def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 
string = "asdfhjikln"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is" , string[index])



5.def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')


6.def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False


 
def postToPre(post_exp):
 
    s = []
 
    length = len(post_exp)
 
    for i in range(length):
 
        if (isOperator(post_exp[i])):
 
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            temp = post_exp[i] + op2 + op1
 
            s.append(temp)
 
        else:
 
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 
# Driver Code
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    print("Prefix : ", postToPre(post_exp))




7.def prefixToInfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            stack.append(prefix[i])
            i -= 1
        else:
           
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 
# Driver code
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))



8.def isBalanced(exp):
 
    flag = True
    count = 0
 
    for i in range(len(exp)):
        if (exp[i] == '('):
            count += 1
        else:
             
            count -= 1
 
        if (count < 0):
 
           
            flag = False
            break
 
    
    if (count != 0):
        flag = False
 
    return flag
 
if __name__ == '__main__':
     
 
    exp1 = "((()))()()"
 
    if (isBalanced(exp1)):
        print("Balanced")
    else:
        print("Not Balanced")
 
    exp2 = "())((())"
 
    if (isBalanced(exp2)):
        print("Balanced")
    else:
        print("Not Balanced")


9.class Stack:
 
    def __init__(self):
        self.Elements = []
         
    def push(self, value):
        self.Elements.append(value)
       
    def pop(self):
        return self.Elements.pop()
     
    def empty(self):
        return self.Elements == []
     
    def show(self):
        for value in reversed(self.Elements):
            print(value)
 
def BottomInsert(s, value):
   
    if s.empty():
         
        
        s.push(value)
         
  
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
 
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 
 
stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()



10.list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest element is:", *list1[:1])