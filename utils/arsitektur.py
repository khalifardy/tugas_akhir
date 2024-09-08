from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, MaxPool1D
from tensorflow.keras.optimizers import Adam
import numpy as np

class StarNet:
    KERNEL_SIZE_DICT = {
        1:16,
        2:24,
        3:32,
        4:40,
        5:48,
        6:52,
        7:64
    }

    ACTIVATION_DICT = {
        1:'relu',
        2:'tanh',
        3:'sigmoid',
        4:'elu',
        5:'selu',
    }

    KERNEL_INITIALIZER = {
        1:'zeros',
        2:'ones',
        3:'random_normal',
        4:'random_uniform',
        5:'truncated_normal',
        6:'variance_scaling',
        7:'orthogonal',
        8:'lecun_normal',
        9:'lecun_uniform',
        10:'glorot_normal',
        11:'glorot_uniform',
        12:'he_normal',
        13:'he_uniform',
    }

    LEARNING_RATE_DICT ={
        1:10**-6,
        2:10**-5,
        3:10**-4,
        4:10**-3,
        5:10**-2,
        6:10**-1,
    }

    RANGE_DICT = {
        'kernel_size':[1,7],
        'activation':[1,5],
        'kernel_initializer':[1,13],
        'learning_rate':[1,6],
        'epoch':[50,100],
        'batch':[0,8],
        'pool_size':[2,9]
        
    }
    
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
    
    def decoding(self,x:np.array):
    
        lower_bond = np.array([1,1,1,1,1,1,2,1,1,1,1,1,1,1,50,0])
        upper_bond = np.array([7,7,5,5,13,13,9,5,5,5,13,13,13,6,100,8])
        delta = (upper_bond - lower_bond)
        term = x * delta
        hasil = lower_bond + term
        return np.int64(np.floor(hasil))
    
    def arsitektur_start_net(self,X_train, y_train, X_test, y_test,k1,k2,a1,a2,ki1,ki2,pz,ad1,ad2,ad3,kid1,kid2,kid3,lr,epoch, batch):
        # Membangun model Sequential
        model = Sequential()

        # Conv Layer 1
        model.add(Conv1D(filters=4, kernel_size=k1, activation=a1, kernel_initializer=ki1,input_shape=(8575, 1)))

        # Conv Layer 2
        model.add(Conv1D(filters=16, kernel_size=k2, activation=a2, kernel_initializer=ki2))

        # Max Pooling
        model.add(MaxPooling1D(pool_size=(pz,)))

        # Flattening
        model.add(Flatten())

        # Fully Connected Layer 1
        model.add(Dense(256, activation=ad1, kernel_initializer=kid1))

        # Fully Connected Layer 2
        model.add(Dense(128, activation=ad2, kernel_initializer=kid2))

        # Output layer untuk empat parameter bintang
        model.add(Dense(4, activation=ad3, kernel_initializer=kid3))

        # Kompilasi model
        model.compile(optimizer=Adam(learning_rate=lr), loss='mean_squared_error')

        # Melatih model
        X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
        X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

        history = model.fit(X_train, y_train, epochs=epoch, batch_size=batch, validation_data=(X_test, y_test))
    
        train_error = history.history['loss'][-1]
        val_error = history.history['val_loss'][-1]
    
        return train_error, val_error
        
    def fitness_function(self,komodo:np.array):
    
        decode_komodo = self.decoding(komodo)
        _,val_error = self.arsitektur_start_net(self.X_train, self.y_train, self.X_test, self.y_test, self.KERNEL_SIZE_DICT.get(decode_komodo[0]), self.KERNEL_SIZE_DICT.get(decode_komodo[1]), self.ACTIVATION_DICT.get(decode_komodo[2]), self.ACTIVATION_DICT.get(decode_komodo[3]), self.KERNEL_INITIALIZER.get(decode_komodo[4]), self.KERNEL_INITIALIZER.get(decode_komodo[5]), decode_komodo[6], self.ACTIVATION_DICT.get(decode_komodo[7]), self.ACTIVATION_DICT.get(decode_komodo[8]), self.ACTIVATION_DICT.get(decode_komodo[9]), self.KERNEL_INITIALIZER.get(decode_komodo[10]), self.KERNEL_INITIALIZER.get(decode_komodo[11]), self.KERNEL_INITIALIZER.get(decode_komodo[12]), self.LEARNING_RATE_DICT.get(decode_komodo[13]), decode_komodo[14], 2**decode_komodo[15])
    
        penyebut = val_error + 10**-8
    
        return 1/penyebut
    
