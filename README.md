
# 🎵 Music Genre Classification with CNNs & HPC

This project demonstrates how to build a fast, scalable pipeline for classifying music genres from raw audio using deep learning and high-performance computing (HPC) techniques.

## 📌 Overview

Traditional deep learning models like RNNs and LSTMs are powerful for time-series tasks but are computationally expensive. This project reimagines the problem using spectrograms and lightweight CNNs, accelerating the process with parallel computing.

## 🧠 Pipeline Architecture

```
Audio (.wav) → Spectrogram (Librosa) → CNN (TensorFlow) → Predicted Genre
```

## 🚀 Key Features

- Convert audio to Mel spectrograms using Librosa
- Train a lightweight CNN on image data
- Parallel preprocessing with `ipyparallel`
- TensorFlow thread-level training optimization
- Achieved 64.5% validation accuracy

## ⚙️ Performance Summary

| Stage          | Task               | Time Reduced       | Speed-up |
|----------------|--------------------|--------------------|----------|
| Preprocessing  | Spectrogram Gen    | 162s → 26s         | 6.16x    |
| Model Training | CNN Optimization   | 6102s → 707s       | 8.6x     |
| **Total Time** | Entire Pipeline    | ~1.73hr → 12min    | **91%**  |

## 📂 Directory Structure

```
.
├── audio_data/               # Input .wav files
├── spectrograms/             # Generated .jpg spectrograms
├── model/                    # CNN architecture and weights
├── notebooks/                # Jupyter notebooks for training and HPC
├── Convert_Audio_File_to_jpg_file/  # Batch preprocessing script
└── README.md
```

## 🧪 How to Run

### 1. Generate Spectrograms
```bash
python Convert_Audio_File_to_jpg_file.py
```

Or using `ipyparallel`:
```python
import ipyparallel as ipp
rc = ipp.Cluster(n=4).start_and_connect_sync()
dview = rc[:]
dview.map_sync(process_audio_file, file_list)
```

### 2. Train the CNN
```python
model.fit(train_generator, validation_data=val_generator, epochs=200)
```

### 3. Predict Genre
```python
pred = model.predict(spectrogram_input)
```

## 🔮 Future Improvements

- Multi-label genre support
- GPU acceleration
- Real-time streaming classification
- API deployment for inference

## 📎 Links

- Medium Write-Up: [Insert Medium URL]
- Banner: Included in repo
- Demo Screenshots: Coming soon

## 📜 License
MIT License
