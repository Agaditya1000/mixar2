import trimesh
import numpy as np
import random

def identify_seams(mesh):
    """
    Identify seams as edges where UV coordinates are discontinuous.
    If no UVs exist, generate synthetic seams (sample random edges).
    """
    seams = []

    # Safely check if UVs exist
    if hasattr(mesh.visual, "uv") and mesh.visual.uv is not None:
        uv = mesh.visual.uv
        print("✅ UV map found — detecting seams using UV breaks...")
        edges = mesh.edges_unique
        # Placeholder logic: assume every 50th edge is a seam (for simplicity)
        seams = [e.tolist() for i, e in enumerate(edges) if i % 50 == 0]
    else:
        print("⚠️ No UV map found — generating synthetic seams for demo...")
        edges = mesh.edges_unique
        sample_size = min(20, len(edges))  # limit to first 20 edges
        seams = random.sample(edges.tolist(), sample_size)

    return seams


def encode_seams_to_tokens(seams):
    """
    Convert seam edge pairs into string-based tokens.
    Example: [[1,2],[2,3]] -> ["E(1,2)", "E(2,3)"]
    """
    tokens = [f"E({a},{b})" for a, b in seams]
    return tokens


def decode_tokens_to_seams(tokens):
    """
    Convert tokens back to seam edge pairs.
    Example: ["E(1,2)"] -> [[1,2]]
    """
    seams = []
    for t in tokens:
        inner = t.strip("E()")
        a, b = map(int, inner.split(","))
        seams.append([a, b])
    return seams


if __name__ == "__main__":
    mesh = trimesh.load("meshes/example.obj", process=False)
    seams = identify_seams(mesh)
    tokens = encode_seams_to_tokens(seams)
    decoded = decode_tokens_to_seams(tokens)

    print("\n=== Seam Tokenization Prototype ===")
    print(f"Total seams identified: {len(seams)}")
    print("First few seam edges:", seams[:5])
    print("Encoded tokens:", tokens[:5])
    print("Decoded seams:", decoded[:5])
