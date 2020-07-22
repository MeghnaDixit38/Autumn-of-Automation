
def is_palindrome(n):
    N=str(n)
    l=len(N)
    for i in range(int(l/2)):
        if N[i]==N[l-i-1]:
            continue
        else:
            return False
            break


D= int(input())
if is_palindrome(D)!=False:
    x=D+1
    while x>D:
         if is_palindrome(x)!=False:
             print(x)
             break
         else:
            x+=1