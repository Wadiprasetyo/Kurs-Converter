import requests

def menu_koverter():
    menu = int(input('Selamat datang\nSilakan pilih konversi yang akan Anda lakukan :\n 1. IDR Indonesia => USD United States\n 2. USD United States => IDR Indonesia\nSilakan pilih nomor : '))
    bank = input('Silakan ketik bank pilihan Anda : ')
    url = 'https://kurs.web.id/api/v1/'+ bank.lower()
    data = requests.get(url)
    data1 = data.json()
    if data1['error'] == 'true':
        print('Data Unknown, Try Again!')
        return(menu_koverter())
    else:
        if menu == 1:
            nominal = int(input('Silakan input nominal yang akan dikonversi : Rp '))
            nilai_konversi = nominal/int(data1['jual'])
            print('Hasil konversi Rp',nominal,'adalah USD',round(nilai_konversi,2),' \nDengan kurs jual =',data1['jual'],'& kurs beli =',data1['beli'])
        if menu == 2:
            nominal1 = int(input('Silakan input nominal yang akan dikonversi : USD '))
            nilai_konversi1 = nominal1*int(data1['beli'])
            print('Hasil konversi USD',nominal1,'adalah Rp',(nilai_konversi1),' \nDengan kurs jual =',data1['jual'],'& kurs beli =',data1['beli'])

menu_koverter()