#!/bin/bash

echo "====================================================="
echo "   HPC Workflow: Tomato Leaf Disease Classification  "
echo "====================================================="
echo "Mengalokasikan Node Superkomputer..."

module load python/3.8
module load cuda/11.2

echo "Memulai eksekusi train_cnn_model.py..."
python train_cnn_model.py

echo "Eksekusi selesai. Membersihkan memori Node HPC."