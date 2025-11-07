🧩 SeamGPT Mesh Preprocessing & Tokenization Prototype

A research-oriented project exploring how 3D mesh data can be normalized, quantized, reconstructed, and represented as discrete seam tokens — similar to the way SeamGPT or geometry-aware transformer models process 3D data.

🚀 Project Overview

This project demonstrates three key stages of 3D mesh understanding:

Mesh Normalization & Quantization
Converts arbitrary 3D meshes into normalized coordinate spaces and quantized forms for efficient representation.

Reconstruction & Error Analysis
Dequantizes and reconstructs meshes, computing reconstruction errors (MSE & MAE).

Seam Tokenization Prototype
Introduces a novel concept — representing mesh seams (edges where UV maps break) as discrete sequential tokens for AI processing.

Visualization
Visualizes mesh seams (real or synthetic) directly on the 3D model using Matplotlib.

📁 Project Structure
mixar2/
├── meshes/
│   └── example.obj                # Input mesh (e.g., teapot)
├── outputs/
│   ├── normalized/                # Normalized meshes
│   ├── quantized/                 # Quantized meshes & metadata
│   ├── reconstructed/             # Reconstructed meshes
│   └── plots/                     # Error comparison plots
├── src/
│   ├── main.py                    # Runs all three main tasks
│   ├── task1_load.py              # Loads mesh & prints statistics
│   ├── task2_normalize_quantize.py# Normalizes & quantizes mesh
│   ├── task3_reconstruct_error.py # Reconstructs mesh & computes MSE
│   ├── utils.py                   # Helper functions (I/O, saving, etc.)
│   ├── seam_tokenization.py       # Prototype for seam token encoding/decoding
│   └── view_seams.py              # Visualizes seams on 3D mesh
├── requirements.txt               # Dependencies
└── README.md                      # (this file)

⚙️ Setup Instructions
1️⃣ Clone or Copy the Repository
cd Desktop
mkdir mixar2
cd mixar2


Place all the src/ files, meshes/, and requirements.txt inside this folder.

2️⃣ Create & Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate        # (Windows)
# or
source venv/bin/activate     # (Mac/Linux)

3️⃣ Install Dependencies
pip install -r requirements.txt


If open3d fails on Python 3.13, use only matplotlib visualization.

4️⃣ Run the Main Pipeline
python -m src.main example.obj


What it does:

Loads meshes/example.obj

Normalizes and quantizes it

Reconstructs it

Computes reconstruction errors

Saves all outputs in the outputs/ folder

5️⃣ Run the Seam Tokenization Prototype
python -m src.seam_tokenization


Output Example:

⚠️ No UV map found — generating synthetic seams for demo...

=== Seam Tokenization Prototype ===
Total seams identified: 20
Encoded tokens: ['E(608,638)', 'E(3433,3453)', 'E(2982,2990)', ...]
Decoded seams: [[608, 638], [3433, 3453], [2982, 2990], ...]

6️⃣ Visualize Seam Edges (Matplotlib)
python -m src.view_seams


Output:

Opens a 3D plot showing your teapot mesh

Highlights seam edges (in red)

📊 Example Results
Stage	Output Example	Description
Normalization	example_minmax.obj, example_unitsphere.obj	Scales mesh within uniform bounds
Quantization	example_quant_minmax.obj	Converts floats → discrete bins
Reconstruction	example_recon_minmax.obj	Rebuilds mesh from quantized data
Error Metrics	example_mse_comparison.png	Compares MSE for each axis
Seam Tokens	['E(1,2)', 'E(2,3)', 'E(4,5)']	Sequential representation of seams
Visualization	3D plot with red lines	Displays seam edges on the mesh
🧠 Research Summary

This project bridges 3D geometry and sequence learning.
The seam tokenization process converts spatial connectivity (mesh seams) into symbolic sequences, enabling language-model-like architectures (e.g., SeamGPT) to process geometric data.
Each token (E(vertex_i, vertex_j)) encodes local topological information, forming the foundation for transformer-based 3D understanding models.

🧾 Example 10-Line Report Summary

This prototype demonstrates SeamGPT-style mesh preprocessing.
Meshes are normalized, quantized, and reconstructed to analyze precision loss.
Seam edges are encoded into token sequences, bridging 3D geometry and language.
Quantized representations enable compact, loss-aware storage.
Seam tokenization captures surface connectivity as discrete tokens.
Decoding restores seam relations, proving reversible representation.
Visualization highlights seam edges on mesh geometry.
The pipeline provides a foundation for transformer-style 3D understanding.
The experiment shows low reconstruction errors (MSE ≈ 1e-5).
Overall, this work demonstrates token-based geometric abstraction for AI models.

🧠 Technologies Used

Python 3.10+

Trimesh – 3D mesh processing

NumPy – numerical operations

Matplotlib – 3D plotting

(Optional) Open3D – interactive 3D viewer

🧩 Future Work Ideas

Incorporate true UV seam detection (via mesh.visual.uv in textured meshes)

Extend tokenization to face adjacency and surface patches

Use transformer models (e.g., GPT-style) to learn from token sequences

Compare seam token embeddings with mesh reconstruction accuracy

👨‍💻 Author

Aditya Kumar Gupta
B.Tech CSE, SRM Institute of Science and Technology
Specializing in Full-Stack Development, Cloud, and AI-based 3D Systems

📜 License

This project is developed for academic and research learning purposes.
You may reuse and modify the code with attribution.