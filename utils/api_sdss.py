import requests
import os

def run_query(sql):
    url = 'https://skyserver.sdss.org/dr17/SkyServerWS/SearchTools/SqlSearch'
    payload = {'cmd': sql, 'format': 'csv'}
    response = requests.get(url,params=payload)
    response.raise_for_status() 
    return response.text

def download_fits_apogee(url,save_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)