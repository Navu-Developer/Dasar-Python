# merubah tipe data

# str ==> int, float, bool
a = '10'
print("tipe data variabel a : ",type(a))
print("tetapi bisa di konversi menjadi : ",type(int(a))) # syarat str harus angka
print("bisa juga dikonversi menjadi : ",type(float(a))) # syarat str harus angka
print("bisa juga dikonversi menjadi : ",type(bool(a))) # Jika str tidak memiliki nilai maka False

# int ==> str, float, bool
a = 10
print("tipe data variabel a : ",type(a))
print("tetapi bisa di konversi menjadi : ",type(str(a)))
print("bisa juga dikonversi menjadi : ",type(float(a)))
print("bisa juga dikonversi menjadi : ",type(bool(a))) # Jika int = 0, maka False

# float ==> str, int, bool
a = 10.0
print("tipe data variabel a : ",type(a))
print("tetapi bisa di konversi menjadi : ",type(int(a)))
print("bisa juga dikonversi menjadi : ",type(str(a)))
print("bisa juga dikonversi menjadi : ",type(bool(a))) # Jika float = 0, maka False

# float ==> str, int, bool
a = False
print("tipe data variabel a : ",type(a))
print("tetapi bisa di konversi menjadi : ",type(int(a)))
print("bisa juga dikonversi menjadi : ",type(str(a))) # nilai bool = str, jika False = False, True = True
print("bisa juga dikonversi menjadi : ",type(float(a))) # Jika bool = False maka float = 0

# Berlaku pada variabel di dalam list juga
L = ['10', 10.0, 10, False]
print("Data dalam list adalah : ",L)
print("type data masing2 variabel : ")
for i in L:
  print("%s \tBertipe\t" %i,type(i))

print("Setelah dikonversi menjadi int : ")
for i in L:
    print("%s \tBertipe\t" %i,type(int(i)))

print("atau bisa per variabel")

# bisa juga mengkonversi sesuai index yang diinginkan
print("tipe data index ke 0 dari list adalah : ",type(L[0]))
terkonversi = int(L[0])
print("setelah dikonversi menjadi index ke 0 menjadi : ",type(terkonversi))
