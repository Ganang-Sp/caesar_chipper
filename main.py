ulangi = True
while ulangi:
	def logo(nama):
		if len(nama) <= 4: 
			logo = [f"""
			______________________________
			|____________________________|
			| TERIMAKASIH TELAH MENCOBA  |
			|       PROGRAM              |
			|	CAESAR CHIPPER       |
			| MAS {nama} 		     |
			|____________________________| 
			|____________________________|
			"""]
			print(logo[0]) 
		elif len(nama) > 4 and len(nama) <= 8:
			logo = [f"""
			______________________________
			|____________________________|
			| TERIMAKASIH TELAH MENCOBA  |
			| PROGRAM CAESAR CHIPPER INI |
			| MAS {nama} 		     |
			|____________________________| 
			|____________________________|
			"""]
			print(logo[0])
	#huruf alphabet
	huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#menangkap masukkan dari pengguna
	n = input("Masukkan Nama Anda : ").upper()
	a = input("Ketik 'encode' untuk enkripsi \nKetik 'decode' untuk dekripsi \n")
	teks = input("Masukkan Pesan : ")
	shift = int(input("(Harus Dalam Bentuk Angka!!!)Masukkan Jumlah Shift : "))
	shift %= 26
	def caesar(teks_pengguna, jumlah_shift, arahan):
		if arahan == "decode":
			jumlah_shift *= -1
		teks_akhir = ""
		for karakter in teks_pengguna:
			if karakter in huruf:	
				posisi = huruf.index(karakter)
				posisi_baru = posisi + jumlah_shift
				teks_akhir += huruf[posisi_baru]
			else:
				teks_akhir += karakter
		print(f"Berhasil mengubah dari {teks} menjadi : {teks_akhir} ")
	logo(nama=n)
	caesar(teks_pengguna=teks,jumlah_shift=shift,arahan=a)
	t_ulangi = input("Ingin Mengulangi program ini lagi nggak ?\nKetik iya/y untuk mengulangi\nKetik tidak/t untuk tidak mengulangi\nJawaban : ")
	if t_ulangi == 'tidak' or t_ulangi == 't':
		ulangi = False
		print("Baiklah kalau seperti itu, Sampai Jumpa dan Jangan Lupa Balik Lagi Ya Awokawok :V")