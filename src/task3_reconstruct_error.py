import numpy as np
import os
import matplotlib.pyplot as plt
from src.utils import save_mesh, ensure_dirs
import trimesh

OUTPUT_BASE = os.path.join(os.path.dirname(__file__), '..', 'outputs')
RECON_DIR = os.path.join(OUTPUT_BASE, 'reconstructed')
PLOT_DIR = os.path.join(OUTPUT_BASE, 'plots')

def denormalize_minmax(deq, meta):
    v_min, v_max = meta["v_min"], meta["v_max"]
    return deq * (v_max - v_min) + v_min

def denormalize_unitsphere(deq_shifted, meta):
    center, max_dist = meta["center"], meta["max_dist"]
    deq = deq_shifted * 2 - 1
    return deq * max_dist + center

def compute_errors(original, reconstructed):
    n = min(len(original), len(reconstructed))  # align if mismatch
    diff = original[:n] - reconstructed[:n]
    mse = np.mean(diff ** 2, axis=0)
    mae = np.mean(np.abs(diff), axis=0)
    return mse, mae

def run_task3(mesh, mesh_name, bins=1024):
    ensure_dirs([RECON_DIR, PLOT_DIR])
    verts = np.asarray(mesh.vertices)
    faces = np.asarray(mesh.faces)

    # Load quantized meshes and metadata
    q_min_file = os.path.join(OUTPUT_BASE, 'quantized', f"{mesh_name}_quant_minmax.obj")
    meta_min_file = os.path.join(OUTPUT_BASE, 'quantized', f"{mesh_name}_meta_minmax.npz")
    q_us_file = os.path.join(OUTPUT_BASE, 'quantized', f"{mesh_name}_quant_unitsphere.obj")
    meta_us_file = os.path.join(OUTPUT_BASE, 'quantized', f"{mesh_name}_meta_unitsphere.npz")

    # Load MIN-MAX mesh
    q_min_mesh = trimesh.load(q_min_file, process=False)
    q_min = np.asarray(q_min_mesh.vertices).astype(np.float64)
    meta_min = dict(np.load(meta_min_file))
    deq_min = q_min / (bins - 1)
    recon_min = denormalize_minmax(deq_min, meta_min)
    save_mesh(recon_min, faces, os.path.join(RECON_DIR, f"{mesh_name}_recon_minmax.obj"))
    mse_min, mae_min = compute_errors(verts, recon_min)

    # Load UNIT-SPHERE mesh
    q_us_mesh = trimesh.load(q_us_file, process=False)
    q_us = np.asarray(q_us_mesh.vertices).astype(np.float64)
    meta_us = dict(np.load(meta_us_file))
    deq_us = q_us / (bins - 1)
    recon_us = denormalize_unitsphere(deq_us, meta_us)
    save_mesh(recon_us, faces, os.path.join(RECON_DIR, f"{mesh_name}_recon_unitsphere.obj"))
    mse_us, mae_us = compute_errors(verts, recon_us)

    # Plot results
    plt.figure(figsize=(6, 4))
    plt.bar(['X', 'Y', 'Z'], mse_min, alpha=0.7, label='Min-Max')
    plt.bar(['X', 'Y', 'Z'], mse_us, alpha=0.5, label='Unit Sphere')
    plt.legend()
    plt.title("Reconstruction MSE per Axis")
    plt.ylabel("Error")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, f"{mesh_name}_mse_comparison.png"))
    plt.close()

    print("\n=== Reconstruction & Error Analysis ===")
    print(f"Min–Max MSE: {mse_min}, MAE: {mae_min}")
    print(f"Unit Sphere MSE: {mse_us}, MAE: {mae_us}")
    print(f"Saved reconstructed meshes to {RECON_DIR}")
