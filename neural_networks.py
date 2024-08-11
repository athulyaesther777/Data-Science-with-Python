from keras.models import Sequential
from keras.layers import Dense

# Define the model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_shape=(10,)))
model.add(Dense(units=10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()

# Assuming X_train and y_train are already defined
# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)
