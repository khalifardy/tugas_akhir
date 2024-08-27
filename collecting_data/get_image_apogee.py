import os
from utils.api_sdss import download_fits_apogee
import pandas as pd
#https://data.sdss.org/sas/dr17/apogee/spectro/redux/dr17/stars/apo1m/

base_url = 'https://data.sdss.org/sas/dr17/apogee/spectro/redux/dr17/'

data = pd.read_csv('collecting_data/sdss_spectra_data_bintang_apogee.csv')

save_dir = 'spectra_images_apogee'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

dictio = {
    'apstar_id': [],
    'file': []
}
    
for _, row in data.iterrows():
    split_str = row['apstar_id'].split('.')
    url = base_url + f"{split_str[2]}/{split_str[1]}/{split_str[3]}/{row['file']}"
    filename = row['apstar_id'].replace('.','_') + '.fits'
    dictio['apstar_id'].append(row['apstar_id'])
    dictio['file'].append(filename)
    try:
        download_fits_apogee(url, os.path.join(save_dir, filename))
        print(f"Downloaded {filename}")
    except Exception as e:
        print(str(e))
        print(f"Failed to download {filename}")
df = pd.DataFrame(dictio)
df.to_csv('collecting_data/file_id.csv', index=False)
print("Download selesai")