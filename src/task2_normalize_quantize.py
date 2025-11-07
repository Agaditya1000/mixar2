import numpy as np
import os
from src.utils import save_mesh, ensure_dirs


OUTPUT_BASE = os.path.join(os.path.dirname(__file__), '..', 'outputs')
NORMALIZED_DIR = os.path.join(OUTPUT_BASE, 'normalized')
QUANTIZED_DIR = os.path.join(OUTPUT_BASE, 'quantized')

def minmax_normalize(vertices):
    v = np.asarray(vertices)
    v_min = v.min(axis=0)
    v_max = v.max(axis=0)
    norm = (v - v_min) / (v_max - v_min)
    meta = {"v_min": v_min, "v_max": v_max}
    return norm, meta

def unit_sphere_normalize(vertices):
    v = np.asarray(vertices)
    center = v.mean(axis=0)
    v_centered = v - center
    max_dist = np.linalg.norm(v_centered, axis=1).max()
    norm = v_centered / max_dist
    meta = {"center": center, "max_dist": max_dist}
    return norm, meta

def quantize(vertices, bins=1024):
    norm = np.clip(vertices, 0.0, 1.0)
    q = np.floor(norm * (bins - 1)).astype(np.int32)
    return q

def run_task2(mesh, mesh_name, bins=1024):
    ensure_dirs([NORMALIZED_DIR, QUANTIZED_DIR])
    vertices = np.asarray(mesh.vertices)
    faces = np.asarray(mesh.faces)

    # Method 1: Min–Max
    norm_minmax, meta_minmax = minmax_normalize(vertices)
    q_minmax = quantize(norm_minmax, bins)
    save_mesh(norm_minmax, faces, os.path.join(NORMALIZED_DIR, f"{mesh_name}_minmax.obj"))
    save_mesh(q_minmax.astype(float), faces, os.path.join(QUANTIZED_DIR, f"{mesh_name}_quant_minmax.obj"))
    np.savez(os.path.join(QUANTIZED_DIR, f"{mesh_name}_meta_minmax.npz"), **meta_minmax)

    # Method 2: Unit Sphere
    norm_us, meta_us = unit_sphere_normalize(vertices)
    norm_us_shifted = (norm_us + 1) / 2.0
    q_us = quantize(norm_us_shifted, bins)
    save_mesh(norm_us, faces, os.path.join(NORMALIZED_DIR, f"{mesh_name}_unitsphere.obj"))
    save_mesh(q_us.astype(float), faces, os.path.join(QUANTIZED_DIR, f"{mesh_name}_quant_unitsphere.obj"))
    np.savez(os.path.join(QUANTIZED_DIR, f"{mesh_name}_meta_unitsphere.npz"), **meta_us)

    print("\nTask 2 completed — Normalized & Quantized meshes saved.")
    return {
        "minmax": {"meta": meta_minmax},
        "unit_sphere": {"meta": meta_us}
    }

if __name__ == "__main__":
    import sys
    import trimesh
    fname = sys.argv[1] if len(sys.argv) > 1 else "example.obj"
    mesh = trimesh.load(os.path.join(os.path.dirname(__file__), '..', 'meshes', fname), process=False)
    run_task2(mesh, os.path.splitext(fname)[0])
