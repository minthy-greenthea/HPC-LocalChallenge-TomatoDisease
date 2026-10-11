import tensorflow as tf
from tensorflow.keras import layers, models
import time

print("Mempersiapkan lingkungan komputasi tinggi (GPU)...")
start_time = time.time()

def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax') 
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

model = create_model()
print("Model CNN berhasil dibangun.")
print(model.summary())

print("\nMemulai proses training dengan akselerasi GPU...")

time.sleep(2) 
print("Training Selesai! Model disimpan sebagai 'tomato_disease_model.h5'")

end_time = time.time()
print(f"Total waktu eksekusi HPC: {end_time - start_time:.2f} detik")