def simulasi_menunggu():
    stok_meja = 2
    
    mahasiswa = ["Andi", "Budi", "Citra", "Deni"]
    pinjam_sekarang = [1, 1, 2, 1] 
    total_butuh = [6, 3, 5, 2]     

    selesai = [False] * len(mahasiswa)
    urutan_aman = []

    print(f"=== SIMULASI PINJAM LAPTOP (Stok Awal: {stok_meja}) ===")
    print("--------------------------------------------------")

    while len(urutan_aman) < len(mahasiswa):
        ada_kemajuan = False
        
        for i in range(len(mahasiswa)):
            if not selesai[i]:
                kekurangan = total_butuh[i] - pinjam_sekarang[i]
                
                print(f"Cek {mahasiswa[i]}:")
                print(f"  Butuh tambahan: {kekurangan} | Stok meja: {stok_meja}")

                if kekurangan <= stok_meja:
                    stok_meja += pinjam_sekarang[i]
                    selesai[i] = True
                    urutan_aman.append(mahasiswa[i])
                    ada_kemajuan = True
                    print(f"  [✓] HASIL: CUKUP! {mahasiswa[i]} selesai. Stok meja jadi: {stok_meja}\n")
                else:
                    print(f"  [!] HASIL: KURANG! {mahasiswa[i]} HARUS MENUNGGU laptop lain balik.\n")
        
        if not ada_kemajuan:
            print("KESIMPULAN: DEADLOCK! Semua orang saling menunggu, tidak ada laptop sisa.")
            return

    print("--------------------------------------------------")
    print(f"SISTEM AMAN. Urutan Berhasil: {' -> '.join(urutan_aman)}")

simulasi_menunggu()