# Tipe Data List pada Python

a = [] # a menampung list kosong
b = [1] # b menampung list dengan elemen integer 1 di index 0
c = ['','5'] # c menampung list dengan elemen string 5 di index 1
d = ['Huruf',1,9.4,True]

# penomoran index pada list python
# [0,1,2,3,4,5,....] dimulai dari 0

print("LIST PADA PYTHON")
print("================")
print("list c berisi : ",c)
# Cetak list c di index ke 0
print("list c index ke 1 : ",c[1])

print("\n")
print("LIST KOSONG PADA PYTHON")
print("=======================")
# Cetak a dengan list kosong
print("list a kosong : ",a)
print("tipe data a : ",type(a))

print("\n")
print("KONVERSI TIPE DATA PADA LIST PYTHON")
print("===================================")
# konversi tipe data pada elemen list
print("b di index ke 0 : ",b[0],", tipe data : ",type(b[0]))
print("bisa dikonversi menjadi",type(str(b[0])))

print("\n")
print("OPERASI ARITMATIKA ANTAR LIST PYTHON")
print("====================================")
hasil = b[0] + int(c[1])
print("Hasil b index 0 + c index 1 : ",b[0],"+",int(c[1]),":",hasil)

print("\n")
print("LIST MENAMPUNG LEBIH DARI 1 TIPE DATA")
print("=====================================")
i = 0
while i < len(d):
    print("d index ke-%d"%i,type(d[i]))
    i+=1

print("\n")
print("FUNGSI PADA PYTHON")
print("==> append, insert, len, del, clear, pop, remove")
print("list a : ",a)
# append : tambah data belakang
a.append(10)
print("a telah di append 10")
print("list a : ",a)

# insert : tambah data setelah index ke - sekian
a.insert(1,6.4) # ke index ke 1 dengan nilai 6.4
print("\na telah di insert elemen 6.4 di index 1")
print("list a : ",a)

# len : menghitung jumlah data pada list
print("\n len data a")
print("jumlah data a : ",len(a))

# del : menghapus list atau element
# del a untuk menghapus variabel list a
del a[0]
print("del a[0] menghapus a di index 0")
print("list a : ",a)

# clear : menghapus isi list
a.append(1); a.append(2); a.append(3); a.append(4)
print("\na di append 1,2,3,4")
print("list a : ",a)
a.clear()
print("a.clear() menghapus seluruh data list a")
print("list a : ",a)

# pop : kegunaan kurang lebih sama dengan del
a.append(1); a.append(2); a.append(3); a.append(4)
print("\na sebelum di pop")
a.pop(1)
print("a.pop(1) menghapus a index ke 1")
print("list a : ",a)

# remove : menghapus elemen
print("\n")
a.append('apasaja')
print("list a : ",a)
a.remove('apasaja')
print("list a di remove('apasaja') : ",a)
