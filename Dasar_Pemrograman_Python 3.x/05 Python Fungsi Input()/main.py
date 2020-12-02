# Membuat fungsi input tanpa promt
a = input() # data berupa str

# Mebuat fungsi input dengan promt
a = input("a : ") # data berupa str

# Membuat fungsi input dengan tipe data int, float, bool

# integer
b = int(input("b : "))

# float
print("Nilai b : ",b,"dengan tipe data ",type(b))
c = float(input("c : "))
print("Nilai c : ",c,"dengan tipe data ",type(b))

# bool
d = bool(int(input("d : ")))
print("Nilai d : ",d,"dengan tipe data ",type(d))
