bulan = ['januari', 'februari', 'Maret', "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

tanggal = int(input("tanggal : "))
bulan1 = int(input("bulan : "))
tahun = int(input("tahun : "))
kabisat = tahun % 4
hari = 0

def _bulan():
    return(bulan[bulan1-1])

if _bulan() == 'februari':
    if kabisat == 0:
        hari = 29
    else:
        hari = 28
if _bulan() != 'februari':
    if (bulan1%2)!=0:
        hari = 31
    else:
        hari = 30


print("tanggal %d/%s/%d"%(tanggal, _bulan(), tahun))
elif tanggal < hari+1:
    print("tanggal valid")
    if kabisat == 0:
        print("ini tahun kabisat")
    elif kabisat != 0:
        print("ini bukan tahun kabisat")
else:
    print("tanggal tidak valid")
