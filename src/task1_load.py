import os
from src.utils import load_mesh, print_vertex_stats, ensure_dirs


INPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'meshes')

def run_task1(mesh_filename):
    """Load and inspect the mesh"""
    path = os.path.join(INPUT_DIR, mesh_filename)
    mesh = load_mesh(path)
    print_vertex_stats(mesh.vertices)
    return mesh

if __name__ == "__main__":
    import sys
    fname = sys.argv[1] if len(sys.argv) > 1 else "example.obj"
    run_task1(fname)
