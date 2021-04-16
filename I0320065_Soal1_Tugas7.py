#count
print("==============count=================")
str = "Selamat Idul Fitri"

sub = "a"
print ("str.count(sub, 4, 16) : ", str.count(sub, 4, 16))
sub = "an"
print ("str.count(sub) : ", str.count(sub))

#center
print("==============center=================")
str = "Makan opor saat Idul Fitri"

print ("str.center(40, 'a') : ", str.center(40, 'a'))
print ("str.center(40) : ", str.center(40))

#capitalize
print("==============capitalize=================")
str ='Semangat mengerjakan tugas prokom!'
s=str.capitalize()
print(s)

#replace
print("==============replace=================")
str = " Durian buah yang enak, pepaya tidak"
s = str.replace ("durian", "pepaya")
print(s)
