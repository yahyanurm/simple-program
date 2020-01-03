"""
program membalik bilangan bulat
"""
reverse=0
num=int(input("Masukkan bilangan : "))
while(num!=0):
    rem=num%10;      
    reverse=reverse*10+rem;    
    num=num//10    
print(reverse)
     

