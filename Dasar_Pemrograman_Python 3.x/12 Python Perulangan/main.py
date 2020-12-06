# Perulangan pada Python
# for, while

# patokan variabel
a = 5

print("FOR LOOP")
# perulangan for
for i in range(a):
    print("ulang ke-%s"%(i+1))

# perulangan cetak kesamping
for i in range(5):
    print("%s"%(i+1), end=' ')
    print(">> ", end='')
print("\n")


print("WHILE LOOP")
# perulangan while
while a <= 7: # operasi pembanding
    print("a = %s"%a)
    a+=1 # ada operasi penugasan

# perulangan cetak kesamping
while a <= 10:
    print("%s"%a, end=' ')
    print("> ", end='')
    a+=1
print("\n")
