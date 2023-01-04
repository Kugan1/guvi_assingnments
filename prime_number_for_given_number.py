
# Python3 program to display Prime numbers till N
  
#function to check if a given number is prime
def isPrime(n):
  #since 0 and 1 is not prime return false.
  if(n==1 or n==0):
    return False
    
  #Run a loop from 2 to n-1
  for i in range(2,n):
    #if the number is divisible by i, then n is not a prime number.
    if(n%i==0):
      return False
    
  #otherwise, n is prime number.
  return True
  
  
  


print("input size :1<=N<=100000")
N = int(input("enter a number: " ))
def Isvalid(N):
   
    if 1<=N and N<=100000 :
       return True
    else:
        print("Enter a valid Number")
        return False
        

Isvalid(N)



# Driver code    
#check for every number from 1 to N
for i in range(1,N+1):
  #check if current number is prime
  if(isPrime(i)):
    print(i,end=" ")
