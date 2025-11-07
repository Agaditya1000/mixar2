from src.task1_load import run_task1
from src.task2_normalize_quantize import run_task2
from src.task3_reconstruct_error import run_task3
import os

def main(mesh_filename="example.obj"):
    print("\n=== Task 1: Load and Inspect Mesh ===")
    mesh = run_task1(mesh_filename)

    print("\n=== Task 2: Normalize and Quantize ===")
    run_task2(mesh, os.path.splitext(mesh_filename)[0])

    print("\n=== Task 3: Reconstruct and Measure Error ===")
    run_task3(mesh, os.path.splitext(mesh_filename)[0])

    print("\n✅ All tasks complete! Check the 'outputs/' folder for results.\n")

if __name__ == "__main__":
    import sys
    fname = sys.argv[1] if len(sys.argv) > 1 else "example.obj"
    main(fname)
