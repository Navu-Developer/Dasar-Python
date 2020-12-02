# Operator biswise / biner
# AND, OR, XOR, Kebalikan, Left Shift, Right Shift

a = int(input("angka : "))
b = int(input("angka : "))
print("\n")

# AND
print("AND")
c = a & b
print("nilai biner %s : " %a,format(a,"08b"))
print("nilai biner %s : " %b,format(b,"08b"))
print("%s & %s : " %(a, b),format(c,"08b"))
print("\n")

# OR
print("OR")
c = a | b
print("nilai biner %s : " %a,format(a,"08b"))
print("nilai biner %s : " %b,format(b,"08b"))
print("%s | %s : " %(a, b),format(c,"08b"))
print("\n")

# XOR
print("XOR")
c = a ^ b
print("nilai biner %s : " %a,format(a,"08b"))
print("nilai biner %s : " %b,format(b,"08b"))
print("%s ^ %s : " %(a, b),format(c,"08b"))
print("\n")

# Kebalikan
print("Kebalikan")
c = ~a
print("nilai biner %s : " %a,format(a,"08b"))
print("c = ~%s, %s : " %(a, c),format(c,"08b"))
print("\n")

# Left Shift
print("Left Shifting")
c = a << 3
print("nilai biner %s : " %a,format(a,"08b"))
print("c = %s << 2, c : " %a,format(c,"08b"))
print("\n")

# Right Shift
print("Right Shifting")
c = a >> 3
print("nilai biner %s : " %a,format(a,"08b"))
print("c = %s >> 2, c : " %a,format(c,"08b"))
print("\n")
