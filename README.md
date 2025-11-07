# 🧩 SeamGPT Mesh Preprocessing & Tokenization Prototype

A research-oriented prototype demonstrating how 3D mesh data can be normalized, quantized, reconstructed, and represented as discrete seam tokens (a step toward SeamGPT-style geometry-aware sequence models).

---

## 🚀 Quick overview

This repository contains a small pipeline for:
- Normalizing meshes into a canonical coordinate frame.
- Quantizing vertex coordinates for compact, discrete representation.
- Reconstructing dequantized meshes and computing reconstruction errors (MSE & MAE).
- A seam-tokenization prototype that represents mesh seam edges as discrete tokens suitable for sequence modelling.
- Basic visualization of seams on the mesh using Matplotlib.

---

## 📁 Project structure

Use this layout when you copy or inspect the repo:

mixar2/
├── meshes/                          # Input meshes (e.g. example.obj)  
├── outputs/                         # All generated outputs  
│   ├── normalized/                  # Normalized meshes  
│   ├── quantized/                   # Quantized meshes & metadata  
│   ├── reconstructed/               # Reconstructed meshes from quantized data  
│   └── plots/                       # Error and comparison plots  
├── src/  
│   ├── main.py                      # Main entrypoint — runs full pipeline  
│   ├── task1_load.py                # Loads mesh & prints statistics  
│   ├── task2_normalize_quantize.py  # Normalizes & quantizes mesh  
│   ├── task3_reconstruct_error.py   # Reconstructs mesh & computes errors  
│   ├── seam_tokenization.py         # Prototype for seam token encoding/decoding  
│   ├── view_seams.py                # Visualizes seams on 3D mesh (Matplotlib)  
│   └── utils.py                     # Helper functions (I/O, saving, helpers)  
├── requirements.txt                 # Python dependencies  
└── README.md                        # This file

---

## ⚙️ Setup & usage

1) Prepare workspace
```bash
# clone or copy files into a folder named mixar2
cd ~/Desktop
mkdir -p mixar2
cd mixar2
# place the repo contents here (src/, meshes/, requirements.txt, README.md)
```

2) Create and activate a virtual environment
```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3) Install dependencies
```bash
pip install -r requirements.txt
```
Note: If open3d fails to install or run on newer Python versions (e.g., 3.13), the visualization scripts fallback to Matplotlib-only mode. See the specific script logs for details.

4) Run the full pipeline (example: process meshes/example.obj)
```bash
python -m src.main meshes/example.obj
```
What this does:
- Loads the specified mesh.
- Normalizes and quantizes vertex positions.
- Reconstructs from quantized values and computes reconstruction metrics (MSE/MAE).
- Saves normalized / quantized / reconstructed meshes and plots to outputs/.

5) Run the seam-tokenization prototype
```bash
python -m src.seam_tokenization
```
Typical output:
- If no UV map is found, the script may generate synthetic seams for demo/visualization.
- Example short output:
  - "Total seams identified: 20"
  - "Encoded tokens: ['E(608,638)', 'E(3433,3453)', ...]"
  - "Decoded seams: [[608, 638], [3433, 3453], ...]"

6) Visualize seam edges (Matplotlib)
```bash
python -m src.view_seams meshes/example.obj
```
This opens a 3D Matplotlib figure showing the mesh and highlighted seam edges.

---

## 📊 Example outputs (what to expect)
- Normalization: example_minmax.obj, example_unitsphere.obj
- Quantization: example_quant_minmax.obj (+ metadata JSON)
- Reconstruction: example_recon_minmax.obj
- Error plots: example_mse_comparison.png
- Seam tokens: list of strings like ['E(1,2)', 'E(2,3)', 'E(4,5)']
- Visualization: 3D plot with seam edges highlighted

---

## 🧠 Short technical summary

- Normalization: centers and scales meshes into a canonical bounding box (min-max or unit sphere options).
- Quantization: maps continuous float coordinates into discrete bins for compact storage and token-friendly representations.
- Reconstruction & error: dequantize the discrete coordinates to floats and compute MSE/MAE per axis to evaluate precision loss.
- Seam tokenization: encodes seam edges as discrete tokens E(v_i, v_j) where v_i and v_j are vertex indices; this converts mesh topological information into a sequential/symbolic form for transformer-like models.

---

## ✅ Notes & next steps

- The README has been reformatted to present a clear, canonical project structure and corrected code block formatting so file trees and command examples render reliably.
- If you'd like, I can:
  - Commit this updated README.md to a branch and open a PR.
  - Expand any section (detailed API of each script, parameter lists, or examples).
  - Add a CONTRIBUTING or DEVELOPMENT.md with coding and testing conventions.

Tell me which of those you want me to do next and I will proceed.
