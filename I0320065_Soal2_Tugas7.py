#program dengan fungsi numerik
print('mencari nilai terendah dan nilai tertinggi pada beberapa nilai')
n = int(input("berapa jumlah data yang akan dimasukkan ?"))
data =[]
i =1
while i <=n:
    a = float(input("nilai ke-{}:".format(i)))
    data.append(float(a))
    i=1+i
print("nilai terendah adalah",min(data))
print("nilai tertinggi adalah",max(data))
print ()
print('menghitung nilai pangkat suatu bilangan')

a= int(input("masukkan angkanya "))
b= int(input("masukkan pangkatnya "))
print(b,"pangkat",a,"adalah",pow(b,a))
print()
print("membulatkan bilangan ke atas dan ke bawah")
import math
a= float(input("masukkan bilangan yang akan dibulatkan "))
print("pembulatan ke atas bilangan tersebut ialah",math.ceil(a))
print("pembulatan ke baah bilangan tersebut ialah",math.floor(a))