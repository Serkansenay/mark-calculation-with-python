#5 sayıdan oluşan bir liste tanımlayın ve ortalamasını bulun
sayi_listesi = [10, 20, 30, 40, 50]
ortalama = sum(sayi_listesi) / len(sayi_listesi)
print("Sayıların ortalaması:", ortalama)


#bir meyve listesinde "muz" varsa "muz var" yazdırın
meyve_listesi = ["elma", "armut", "muz", "çilek"]
if "muz" in meyve_listesi:
    print("Muz var")



#içinde 1-10 arası sayılar olan bir liste oluşturun ve sadece çift sayıları yazdırın
sayi_listesi = list(range(1, 11))
for sayi in sayi_listesi:
    if sayi % 2 == 0:
        print(sayi)



#iç içe listeyle 3 öğrencinin ad ve notlarını saklayın, her öğrenciyi ekrana yazdırın
ogrenciler = [
    {"ad": "Ali", "not": 85},
    {"ad": "Ayşe", "not": 90},
    {"ad": "Mehmet", "not": 75}
]
for ogrenci in ogrenciler:
    print("Öğrenci Adı:", ogrenci["ad"], "| Notu:", ogrenci["not"])