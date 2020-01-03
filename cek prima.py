"""
Program untuk cek bilangan prima atau bukan
"""
def cekprima(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
bil=int(input("masukkan bilangan : "))
print(cekprima(bil))
