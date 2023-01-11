from models import daftar_nilai
from views import input_nilai
from views import view_nilai as nilai

if __name__ == '__main__':
    no = 0

    while True:
        # opsi input pilihan T,L,U,H,C,K
        tanya = input(
            "(T) Tambah data, | (L) Lihat semua data, | (U) Ubah data, | (H) Hapus data, | (C) Cari data, | (K) Keluar program : \n")
        if tanya in ("t", "T"):
            # melakukan perulangan hingga user memilih n maka perulangan akan berhenti
            while True:
                no += 1
                # memanggil fungsi tambahData dan memparsing data no
                input_nilai.input_data(no)
                print("y or more] Tambah data, n] stop ")
                tambahDataLagi = input("Tambah data lagi ? (y/n) :")
                if tambahDataLagi == 'n':
                    break
            # jika tanya == L maka lihat semua data
        elif tanya in("l", "L"):
            # menampilkan data dalam bentuk table menggunakan package tabulate
            nilai.cetak_daftar_nilai()
            # jika tanya == U maka edit data
        elif tanya in ("u", "U"):
            daftar_nilai.ubah_data()
            # jika tanya == H maka hapus data
        elif tanya in ("h", "H"):
            daftar_nilai.hapus_data()
            # jika tanya == C maka Cari data
        elif tanya in ("c", "C"):
            daftar_nilai.cari_data()
        # jika tanya == K maka keluar dari program
        elif tanya in ("k", "K"):
            print("")
            print("Anda telah keluar dari program.")
            break