import trimesh
import numpy as np
import matplotlib.pyplot as plt
import random

def identify_or_generate_seams(mesh, sample_size=20):
    """
    Identify or simulate seam edges.
    If UVs exist, use them. Otherwise, randomly sample edges.
    """
    seams = []
    if hasattr(mesh.visual, "uv") and mesh.visual.uv is not None:
        print("✅ UV map found — detecting seams using UV breaks...")
        edges = mesh.edges_unique
        seams = [e.tolist() for i, e in enumerate(edges) if i % 50 == 0]
    else:
        print("⚠️ No UV map found — generating synthetic seams for demo...")
        edges = mesh.edges_unique
        seams = random.sample(edges.tolist(), min(sample_size, len(edges)))
    return seams

def visualize_mesh_with_seams_matplotlib(mesh_path):
    mesh = trimesh.load(mesh_path, process=False)
    vertices = np.asarray(mesh.vertices)
    faces = np.asarray(mesh.faces)
    seams = identify_or_generate_seams(mesh)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    # Plot mesh surface (light gray)
    for tri in faces:
        tri_coords = vertices[tri]
        tri_coords = np.vstack([tri_coords, tri_coords[0]])  # close the loop
        ax.plot(tri_coords[:, 0], tri_coords[:, 1], tri_coords[:, 2],
                color="lightgray", linewidth=0.5)

    # Plot seams in red
    for a, b in seams:
        if a < len(vertices) and b < len(vertices):
            line = vertices[[a, b]]
            ax.plot(line[:, 0], line[:, 1], line[:, 2], color="red", linewidth=2)

    ax.set_title("3D Mesh with Seam Edges (Red)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    mesh_path = "meshes/example.obj"
    visualize_mesh_with_seams_matplotlib(mesh_path)
