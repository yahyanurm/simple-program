"""
Program menghitung jumlah digit suatu bilangan
"""
jum=0
num=int(input("Masukkan bilangan : "))
a=str(num)
while(num!=0):
    jum+=num%10
    num=num//10
jum=str(jum)
print("jumlah digit dari {} adalah {}".format(a,jum))
