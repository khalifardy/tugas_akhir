from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

def arsitektur_start_net(X_train, y_train, X_test, y_test):
    # Membangun model Sequential
    model = Sequential()

    # Conv Layer 1
    model.add(Conv1D(filters=4, kernel_size=3, activation='relu', input_shape=(8575, 1)))

    # Conv Layer 2
    model.add(Conv1D(filters=16, kernel_size=3, activation='relu'))

    # Max Pooling
    model.add(MaxPooling1D(pool_size=4))

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