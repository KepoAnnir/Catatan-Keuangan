pemasukan = 0
pengeluaran = 0

while True:
    print("-- CATATAN KEUANGAN --") 
    print("1. Catat Pemasukan") 
    print("2. Catat Pengeluaran") 
    print("3. Liat Pemasukan & Pengeluaran") 
    print("0. Exit") 
    
    pilih = input("Pilih Menu: ")
    
    if pilih == "1":
        try:
            jumlah_Pm = int(input("\nJumlah Pemasukan: ")) 
            pemasukan = pemasukan + jumlah_Pm
            print(pemasukan) 
        except ValueError:
            print("Wajib Angka!")
            continue
    elif pilih == "2":
        try:
            jumlah_Pg = int(input("\nJumlah Pengeluaran: ")) 
            pengeluaran = pengeluaran + jumlah_Pg
            print(pengeluaran) 
        except ValueError:
            print("Wajib Angka!")
            continue           
    elif pilih == "3":
        print("\n-- PEMASUKAN --")   
        print(pemasukan) 
        
        print("\n-- PENGELUARAN --") 
        print(pengeluaran) 
    else:
        break     