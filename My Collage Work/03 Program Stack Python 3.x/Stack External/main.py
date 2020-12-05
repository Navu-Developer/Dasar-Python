# Stack Internal
# Code  : Python3

def main():
    keep_alive = 0
    item = []
    while keep_alive == 0:    
        print("="*25)
        print("PROGRAM STACK INTERNAL")
        print("Code\t: Python3")
        print("="*25)
        for i in item:
            print(i, end=' ')
            print(end=',')
        print("panjang data : ",len(item))
        print('\n')
        print("1. tambah data")
        print("2. hapus data")
        print("0. exit")
        choose = str(input("> "))
        if choose == "1":
            item.append(str(input()))
        if choose == "2":
            item.pop()
        if choose == "0":
            keep_alive+=1
if __name__ == "__main__":
    main()
