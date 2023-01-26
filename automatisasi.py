import requests
import csv
import os
import pandas as pd
import shutil

# Memeriksa folder
if not os.path.exists('hasil'):
    os.makedirs('hasil')

# Menginputkan Keyword    
key = input('masukan keyword :')

# Membuat file csv
write = csv.writer(open('hasil/{}.csv'.format(key), 'w'))

# Membuat header
header = ['nama', 'Harga', 'Stock']
write.writerow(header)

# Menyimpan URL dan menghitung jumblah produk
url = 'https://api.bukalapak.com/multistrategy-products'
count= 0

# Melakukan Loop
for page in range (1,11): 
    parameter = {
        'category_id': 280,
        'sort': key,
        'limit': 50,
        'offset': 0,
        'facet': True,
        'page': page,
        'shouldUseSeoMultistrategy': False,
        'isLoggedIn': True,
        'show_search_contexts': True,
        'access_token':'-YH1XTmCU4-J1cmc7oHEWlXCBjYlLCgCepMMtFZ1fX8tPA'
        }

# Mengambil data Json
    r = requests.get(url, params=parameter).json()
    products = r['data']
    for p in products :
        nama = p['name']
        harga = p['price']
        jumblah_barang = p['stock']
        count+=1
        print('no:',count,' nama: ' ,nama , 'harga: ',harga,'jumblah: ',jumblah_barang )

# Menambahkan counter
        write = csv.writer(open('hasil/{}.csv'.format(key),'a'))
        data = [nama, harga, jumblah_barang]
        write.writerow(data)
        
# Membaca data dari file CSV
data = pd.read_csv('hasil/{}.csv'.format(key))

# Menulis data ke file Excel
data.to_excel('hasil/{}.xlsx'.format(key), index=False)

# Membuat file zip
shutil.make_archive('hasil', 'zip', 'hasil')