import numpy as np
import trimesh
import os

def ensure_dirs(paths):
    """Create directories if they don't exist"""
    for p in paths:
        os.makedirs(p, exist_ok=True)

def load_mesh(path):
    """Load mesh from .obj file"""
    mesh = trimesh.load(path, process=False)
    if hasattr(mesh, 'vertices'):
        return mesh
    else:
        raise ValueError(f"Failed to load mesh from {path}")

def save_mesh(vertices, faces, path):
    """Save vertices and faces as .obj mesh"""
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)
    mesh.export(path)
    print(f"Saved mesh to {path}")
    return path

def print_vertex_stats(vertices):
    """Print basic vertex statistics"""
    v = np.asarray(vertices)
    print("\nMesh Statistics:")
    print("Vertices:", v.shape[0])
    print("Min per axis:", v.min(axis=0))
    print("Max per axis:", v.max(axis=0))
    print("Mean per axis:", v.mean(axis=0))
    print("Std per axis:", v.std(axis=0))
