#!/usr/bin/env python3
import os
import shutil
import sys

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_filename = "entry.png"
    src_path = os.path.join(script_dir, src_filename)
    target_filename = "entry.png"

    if not os.path.exists(src_path):
        print(f"Error: {src_filename} not found in {script_dir}.", file=sys.stderr)
        sys.exit(1)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
        dest_path = os.path.join(output_dir, target_filename)
        shutil.copyfile(src_path, dest_path)
        print(f"Successfully copied {src_filename} to {dest_path}")
    except OSError as e:
        print(f"Warning: Could not write to {output_dir} ({e}). Falling back to local 'output' directory.", file=sys.stderr)
        fallback_dir = os.path.join(script_dir, "output")
        os.makedirs(fallback_dir, exist_ok=True)
        dest_path = os.path.join(fallback_dir, target_filename)
        shutil.copyfile(src_path, dest_path)
        print(f"Successfully copied {src_filename} to {dest_path}")

if __name__ == "__main__":
    main()
