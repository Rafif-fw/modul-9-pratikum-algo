# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:15:37 2022

@author: Rafif Fernanda
"""

def buatFile():
    file = open("modul9_3.txt", "w")
    namaa = input("Masukkan Nama:")
    nim = input("Masukkan NIM:")
    angkatan = input("Masukkan Angkatan:")
    file.write("Nama: " + namaa)
    file.write("\nNIM " + nim)
    file.write("\nAngkatan: " + angkatan)
    file.close()
    
def bacaFile():
    file = open("modul9_3.txt", "r")
    text = file.read()
    print(text)
    file.close()
    
def updateFile():
    file = open("modul9_3.txt", "a")
    sahabat = input("Masukkan nama sahabatmu: ")
    catatan = input("Masukan catatan tambahan: ")
    file.write("\nSahabat:" + sahabat)
    file.write("\nCatatan:" + catatan)
    file.close()
    
def main():
    repeat = True
    while (repeat):
        print("=== Program File Handling - Rafif")
        print("1. Membuat & Menulis FIle")
        print("2. Membaca File")
        print("3. Update File")
        print("4. Keluar dari program")
        pilih = int(input("Masukkan nomor pilihan Anda:"))
        
        if (pilih == 1):
            print("\n")
            buatFile()
            print("\n")
        elif (pilih == 2):
            print("\n")
            bacaFile()
            print("\n")
        elif (pilih == 3):
            print("\n")
            updateFile()
            print("\n")
        elif (pilih == 4):
            print("Terima kasih telah menggunakan program saya")
            repeat = False
        else:
            print("Masukkan nomor yang ada list!")
            print("\n")
            
main()
            
            
            
            