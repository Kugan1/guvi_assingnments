# Guvi_Assingnments
**1.given a string S convert each of the charecters into numbers(ASCII) and print the sum of numbers**

EXAMPLE :\
Input: abc\
Output: 294
 
**2.Given a number N, print all prime numbers less than N(in ascending order)**
input size 1<=N<=100000\
EXAMPLE:\
input:10\
output:2 3 5 7


**3.Email Validation:**

Given a string S check if is a valid email id based on the following Conditions\

1)@should be present;\
2)@ & should not be repeated;\
3)there should be atleast four characters between @ and .;\
4)there should be at-least 3 characters before @\
5)the end of mail id should be .com: If its a valid email id print\
YES' else print "NO".\
input size: |S|<=100000\
EXAMPLE:\
INPUT:\
test@gmail.com\
OUTPUT:\
YES


**4.Consider today is Sunday, In a restaurant, too much crowd in the cash counter the cashier needs some help to calculate the bills. that restaurant has different recipes they are,**\
Menu:-\
oniondosa-90 rs\
plaindosa-40 rs\
ravadosa-75 rs\
idli-10 rs\
vada-5 rs\
poori-30 rs\
chapathi -30 rs\
pongal-35 rs\
tea-25 rs\
coffee-35 rs\
meals-75 rs

Note: The price detalls described above is without GST. You need to add 5 percent of GST for the total amount of a bill.
If there is no recipe in the menu, print "Sorry, Only recipes on the menu!"\
**Input:**\
 Single line consists of recipes in string and with count in Integer as shown
below.\
**Output:**\
Print output as "Total Price(GST inclusive):Rs xx.x\
Sample Testcase:\
**Input:**\
vada 2 coffee 1\
**Output:**\
Total Price(GST inclusive):Rs 47.25\
**sample input:**\
tea 2\
**sample output:**\
Total Price(GST inclusive) : Rs 52.5\
**sample input:**\
vada 2 coffee 1\
**sample output:**\
Total Price(GST inclusive) Rs 47.25\
**sample input:**\
masaladosa 1\
**sample output:**\
Sorry, Only recipes on the monu!

**5.An interview is scheduled for a list of students in GUVI Office,and the candidate list has been shared to the interview panel.\
But in the last minute HR came to know the last n students in the candidate list need to be given priority,since they need to catch a flight.**

For Example, with n=7 candidates and k=3 need to catch their flight So the order need to be changed as\
(1,2,3,4,5,6,7)to(5,6,7,1,2,3,4).\
If k <=0,no shuffling is needed.\
Write a program to help the HR to shuffle the candidate list so that last in will come in the first.

Input:\
n-No. of candidates\
k-No. of candidates in the end of the list who need to be given priority\
a[n]-Candidates list\
Output:\
Candidates list in shuffled order\
**Sample Input1:**\
7\
3\
1 2 3 4 5 6 7\
**Output:**\
5 6 7 1 2 3 4

**Sample Input2:**\
8\
5\
10 20 30 40 50 60 70 80\
**Output:**\
40 50 60 70 80 10 20 30
