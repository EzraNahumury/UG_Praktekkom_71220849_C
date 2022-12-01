def penjumlahan (tiga,satu):
    hasil = tiga + satu
    return hasil

def penngurangan (tiga,satu):
    hasil = tiga - satu
    return hasil

def perkalian (tiga,satu):
    hasil = tiga * satu
    return hasil

def pembagian  (tiga,satu):
    hasil = tiga / satu
    return hasil

print ("===================")
print ("Operasi Matematika")
print ("1. Jumlah    [+]")
print ("2. Kurang    [-]")
print ("3. Kali      [*]")
print ("4. Bagi      [/]")
print ("===================")
operasi = input("(Pilih operasi :1/2/3/4) : ")
print ("===================")
satu=eval(input("Masukkan Bilangan Pertama :"))
dua=eval(input("Masukkan Bilangan Kedua :"))

if operasi == '1':
    print (f"Hasil Operasi dari",satu,"+",dua,"=",penjumlahan(satu,dua))
elif operasi == '2':
    print (f"Hasil Operasi dari",satu,"-",dua,"=",pengurangan(satu,dua))
elif operasi == '3':
    print (f"Hasil Operasi dari",satu,"*",dua,"=",perkalian(satu,dua))
elif operasi == '4':
    print (f"Hasil Operasi dari",satu,"/",dua,"=",pembagian(satu,dua))


def penjumlahan (tiga,satu):
    hasil = tiga + satu
    return hasil

def penngurangan (tiga,satu):
    hasil = tiga - satu
    return hasil

def perkalian (tiga,satu):
    hasil = tiga * satu
    return hasil

def pembagian  (tiga,satu):
    hasil = tiga / satu
    return hasil

print ("===================")
print ("Operasi Matematika")
print ("1. Jumlah    [+]")
print ("2. Kurang    [-]")
print ("3. Kali      [*]")
print ("4. Bagi      [/]")
print ("===================")
operasi = input("(Pilih operasi :1/2/3/4) : ")
print ("===================")
satu=eval(input("Masukkan Bilangan Pertama :"))
dua=eval(input("Masukkan Bilangan Kedua :"))

if operasi == '1':
    print (f"Hasil Operasi dari",satu,"+",dua,"=",penjumlahan(satu,dua))
elif operasi == '2':
    print (f"Hasil Operasi dari",satu,"-",dua,"=",pengurangan(satu,dua))
elif operasi == '3':
    print (f"Hasil Operasi dari",satu,"*",dua,"=",perkalian(satu,dua))
elif operasi == '4':
    print (f"Hasil Operasi dari",satu,"/",dua,"=",pembagian(satu,dua))





