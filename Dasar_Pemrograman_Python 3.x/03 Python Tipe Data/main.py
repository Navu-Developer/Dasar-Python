# tipe data
'''
angka = integer / int (tanpa titik {Dalam python titik adalah koma})
teks = string / str (penulisan variabel dengan petik {contoh: 'string'})
desimal = float / float (sama seperti angka hanya dengan titik {contoh: 10.5})
cek = boolean / bool (bernilai True atau False)
sekuensial = list, tuple (data berurutan)  
'''

# data integer / int
a = 1000
print("Nilai variabel a : ",a)
print("variabel a bertipe data : ",type(a))

# data string / str
teks = 'seribu'
print("Nilai variabel teks : ",teks)
print("variabel teks bertipe data : ",type(teks))

# data desimal / float
b = 1000.0
print("Nilai variabel b : ",b)
print("variabel b bertipe data : ",type(b))

# tipe data boolean
salah = True
benar = False
print("Nilai variabel salah : ",salah)
print("Nilai variabel benar : ",benar)
print("variabel salah bertipe data : ",type(salah))
print("variabel benar bertipe data : ",type(benar))

# tipe data list
list_anda = ['seribu',1000,1000.0] # index = 0 > 1 > 2
print("Nilai variabel list_anda : ",list_anda)
print("variabel list_anda bertipe data : ",type(list_anda))

# list bisa berisi berbagai tipe data variabel
a = list_anda[0] # a bernilai = list_anda index ke 0
b = list_anda[1] # b bernilai = list_anda index ke 1
c = list_anda[2] # c bernilai = list_anda index ke 2
print("variabel a = list_anda index ke 0 : ",a)
print("variabel b = list_anda index ke 0 : ",b)
print("variabel c = list_anda index ke 0 : ",c)
print("variabel a bertipe data : ",type(a))
print("variabel b bertipe data : ",type(b))
print("variabel c bertipe data : ",type(c))
