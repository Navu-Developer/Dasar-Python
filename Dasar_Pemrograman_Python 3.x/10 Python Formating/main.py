# Formating pada Python
# .format()
# %s (string) %d (int) %f (float)

a = '<nama saya>'
b = 15
c = 170.5

print("Nama saya %s, umur saya %d, tinggi saya %f cm" %(a, b, c))
print("="*20)
print("\nNama saya",type(a),", umur saya",type(b),", tinggi saya",type(c),"cm")
print("="*20)

# menggunakan konversi tipe data pada formating

b = float(b)
c = int(c)
print("Nama saya %s, umur saya %d, tinggi saya %f cm" %(a, b, c))
print("="*20)
print("\nNama saya",type(a),", umur saya",type(b),", tinggi saya",type(c),"cm")
print("="*20)

c = 170.5
# formating float
print("\nTinggi saya : ",c)
print("="*20)
print("Tinggi saya : {:.0f}".format(float(c)))
