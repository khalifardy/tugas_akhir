#import requests
#import pandas as pd
#import os
import sys
import os

# Menambahkan direktori 'tugas_akhir' ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import io
import csv
from utils.api_sdss import run_query

    
#membuat direktori untuk menyimpan spektrum

    
query = """
SELECT TOP 5000 *
FROM apogeeStar at INNER JOIN 
aspcapStar asr ON at.apogee_id = asr.apogee_id
where at.starflag = 0 
and at.vscatter < 1 and at.rv_logg != -9999 and at.SNR > 200 and asr.aspcapflag =0
and asr.vsini != -9999 and at.telescope = 'apo25m' and m_h != -9999
"""



csv_data = run_query(query)
csv_filename = 'sdss_spectra_data_bintang_apogee.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Membaca baris data dari hasil query
    csvreader = csv.reader(io.StringIO(csv_data))
    
    # Tulis setiap baris ke file CSV
    for row in csvreader:
        writer.writerow(row)

# Mendownload setiap spektrum dalam bentuk gambar
#for sd in df:
    #print(sd)
    