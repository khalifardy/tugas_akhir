import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from astropy.io import fits


def inputx_outputy(file_1,file_2,folder_path):

    df = pd.read_csv(file_1)
    df2 = pd.read_csv(file_2)
    y = []
    x = []
    
    for filename in os.listdir(folder_path):
        temp_y = []
        if os.path.isfile(os.path.join(folder_path,filename)):
            #print(f"nama file: {filename}")
            flux = fits.getdata(f"{folder_path}/{filename}")
            hdr = fits.getheader(f"{folder_path}/{filename}")
            nf = len(flux[0])
            crval = np.double(hdr['CRVAL1'])
            cdelt = np.double(hdr['CDELT1'])
            ws = np.empty(nf)
            for k in range(nf):
                ws[k] = crval + (cdelt*k)
            ws = 10.0**ws
            ws = ws - ((hdr['VHELIO']/299792.458e0)*ws)
            id_star = df2.loc[df2['file'] == filename].get('apstar_id').values[0]
            result = df.loc[df['apstar_id']==id_star]
            
            teff = result.get('teff').values[0]
            logg = result.get('logg').values[0]
            vsin1 = result.get('vsini').values[0]
            m_h = result.get('m_h').values[0]
            temp_y = [teff,logg,vsin1,m_h]
            y.append(temp_y)
            x.append(flux[0])
    
    return np.array(x),np.array(y)

def convert_to_jpg(folder_path):
    
    for filename in os.listdir(folder_path):
        
        if os.path.isfile(os.path.join(folder_path,filename)):
            print(f"nama file: {filename}")
            flux = fits.getdata(f"{folder_path}/{filename}")
            hdr = fits.getheader(f"{folder_path}/{filename}")
            nf = len(flux[0])
            crval = np.double(hdr['CRVAL1'])
            cdelt = np.double(hdr['CDELT1'])
            ws = np.empty(nf)
            for k in range(nf):
                ws[k] = crval + (cdelt*k)
            ws = 10.0**ws
            ws = ws - ((hdr['VHELIO']/299792.458e0)*ws)
            judl = filename.replace("_",".")
            judl = judl.replace(".fits","")
            plt.title(f"{judl.replace('.',' ')}")
            plt.ylabel('relative flux')
            plt.xlabel('wavelength (Angstroms)')
            plt.plot(ws,flux[0])
            os.makedirs("file_image", exist_ok=True)
            filepath = os.path.join("file_image", f"{judl.replace(".","_")}.png")
            plt.savefig(filepath)
            plt.clf()
        
        
       
 
        
        
        

        
        
        