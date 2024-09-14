import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('coba_full.ipynb'), '..')))

from  utils.utilitas import convert_to_jpg

folder_path = 'spectra_images_apogee'

convert_to_jpg(folder_path)
print("convert selesai")