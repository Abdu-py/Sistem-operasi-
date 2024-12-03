print("Peehitungan Luas Persegi")
print("====================")	
print("Nilai Sisi / Luas")

for sisi in range(1, 11):
	luas = sisi * sisi
	print(f"{sisi:6}{luas:10}")
print("  ")
	
def hitung_luas_persegi(sisi):
    return sisi * sisi

def main():
    print("Kesimpulan Dari Perhitungan Luas Persegi Diatas =")
    print("=========================")
    for sisi in range(1, 11):
        luas = hitung_luas_persegi(sisi)
        print(f"Luas persegi dengan sisi {sisi} adalah {luas}")

if __name__ == "__main__":
	main()

