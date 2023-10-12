n=int(input("enter a number:"))
def armstrong (n):
  sum=0
  temp=n
  while temp>0:
   digit=temp%10
   sum=sum+digit**3
   temp//=10
  if n==sum:
    print(n,"is an Armstrong number")
  else:
    print(n,"is not an Armstrong number")
armstrong(n)
#153,371,
def reverse(n):
   rev = 0
   while n>0:
     rem=n%10
     rev=(rev*10)+rem
     n=n//10
   return rev
temp=n
res=reverse(tmp)
print("n=",tmp)
print("rev=",res)
if(n==res):
print("palindrome")
else:
print("Not a palindrome")
