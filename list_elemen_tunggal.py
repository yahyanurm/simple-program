"""
Mencari list dengan elemen unik
"""
l=[1,1,2,2,2,3,3,3,4,4]
l_baru=[]
for i in l:
    if i not in l_baru:
        l_baru.append(i)
print(l_baru)
