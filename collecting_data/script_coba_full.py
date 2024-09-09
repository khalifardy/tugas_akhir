import os
import sys
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('coba_full.ipynb'), '..')))

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from astropy.wcs import WCS
import pandas as pd
from scipy import interpolate
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

#library lokal
from  utils.utilitas import inputx_outputy
from utils.arsitektur import StarNet
from utils.kma_method import KomodoMlipirAlgorithm
from utils.pre_processing import interpolate_nan, normalize_flux_minmax

#dapatkan data x dan y dimana x adalah flux dan y adalah vektor teff, logg, feh dan vin sin 1

name_file_1 = 'sdss_spectra_data_bintang_apogee.csv'
name_file_2 = 'file_id.csv'
folder_path = 'spectra_images_apogee'

x,y = inputx_outputy(name_file_1, name_file_2, folder_path)

#interpolasi nilai nan
for i in range(len(x)):
    x[i] = interpolate_nan(x[i])
    x[i] = normalize_flux_minmax(x[i])

#split data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Arsitektur tanpa optimasi KMA

#Membangun model Sequential
model = Sequential()

# Conv Layer 1
model.add(Conv1D(filters=4, kernel_size=3, activation='relu', input_shape=(8575, 1)))

# Conv Layer 2
model.add(Conv1D(filters=16, kernel_size=3, activation='relu'))

# Max Pooling
model.add(MaxPooling1D(pool_size=7))

# Flattening
model.add(Flatten())

# Fully Connected Layer 1
model.add(Dense(256, activation='relu'))

# Fully Connected Layer 2
model.add(Dense(128, activation='relu'))

# Output layer untuk empat parameter bintang
model.add(Dense(4, activation='linear'))

# Kompilasi model
model.compile(optimizer='adam', loss='mean_squared_error')

# Melatih model
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))


#inisisai fungsi fitness

start_net = StarNet(X_train, y_train, X_test, y_test)

search_space = {
    'k1':[0,1],
    'k2':[0,1],
    'a1':[0,1],
    'a2':[0,1],
    'ki1':[0,1],
    'ki2':[0,1],
    'pz':[0,1],
    'AD1':[0,1],
    'AD2':[0,1],
    'AD3':[0,1],
    'KID1':[0,1],
    'KID2':[0,1],
    'KID3':[0,1],
    'lr':[0,1],
    'epoch':[0,1],
    'batch':[0,1]
}

#inisiasi kmh 

n = 5
p = 0.5
d = 0.1
max_iter = 5
fitness_function = start_net.fitness_function


kma = KomodoMlipirAlgorithm(n,p,d,fitness_function,search_space,max_iter)
start = datetime.datetime.now()
hasil = kma.optimize()
end = datetime.datetime.now()
delta = end - start

print(delta.total_seconds())
print(kma.history)
print(hasil)