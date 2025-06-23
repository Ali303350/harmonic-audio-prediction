# Project: Machine Learning Audio Analysis

This project performs signal processing and basic audio analysis using Python. It includes tools to load `.wav` files, extract features such as pitch (F0), perform harmonic and LPC analysis, and visualize results. It is designed for learning and experimentation with real-world audio recordings.

## 📁 Project Structure 

project_machine_learning/
├── main.py # Main script to run the analysis
├── data/ # Directory for input .wav files
│ ├── rec1.wav
│ └── rec2.wav
├── src/ # Source code
│ ├── init.py
│ ├── audio_processing/ # Functions related to loading and segmenting audio
│ │ ├── init.py
│ │ ├── load_wav.py
│ │ └── select_segment.py
│ ├── analysis/ # Audio analysis functions
│ │ ├── init.py
│ │ ├── compute_periodogram.py
│ │ ├── estimate_f0_autocorr.py
│ │ ├── fit_harmonics.py
│ │ ├── lpc_analysis.py
│ │ └── compare_recordings.py
│ └── visualization/ # Plotting functions
│ ├── init.py
│ ├── plot_waveform.py
│ ├── plot_periodogram.py
│ ├── plot_original_vs_harmonic_fit.py
│ ├── plot_harmonic_energy_vs_f0.py
│ ├── plot_harmonic_coefficients.py
│ ├── plot_lpc.py
│ ├── plot_lpc_coefficients.py
│ └── plot_lpc_error_vs_order.py
├── requirements.txt # Required Python libraries
└── README.md # Project documentation

## ⚙️ Setup Instructions

1. **Create and activate a virtual environment**  

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. **Install dependencies**  

    pip install -r requirements.txt

3. **Add your audio files**

    Place your .wav files inside the data/ folder:
    data/rec1.wav
    data/rec2.wav

**How to Run**

Run the main script from the root folder:

    python main.py

    The script will load your recordings, analyze them, and display a variety of plots such as waveforms, frequency content, and model approximations.

**Features**

- Load and visualize audio signals

- Extract and analyze signal segments

- Frequency-domain analysis using periodograms

- Fundamental frequency estimation (F0) using autocorrelation

- Harmonic model fitting and visualization

- LPC (Linear Predictive Coding) analysis and plots

- Compare features across multiple recordings

**Requirements**

All dependencies are listed in requirements.txt. Key libraries include:

- numpy

- scipy

- matplotlib

- soundfile (optional for some audio formats)

**Notes**

- Make sure the audio file names match what is used in main.py.

- You can modify or extend this project by adding more analysis or visualization scripts under the src/ directory.



