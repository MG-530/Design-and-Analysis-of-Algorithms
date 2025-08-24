import os
import subprocess
import time
import csv
import sys

# List of algorithm directories to process based on the README.md file.
ALGORITHM_DIRS = [
    "01-strassen",
    "02-product-of-two-polynomials",
    "03-product-of-two-big-numbers",
    # "04-recursive-sum",
    # "05-recursive-factorial",
    # "06-recursive-power",
    # "07-recursive-quotient",
    # "08-recursive-remainder",
    # "09-recursive-gcd",
    # "10-recursive-combination",
    # "11-tower-of-hanoi",
    # "12-iterative-binary-search",
    # "13-recursive-binary-search",
    # "14-interpolation-Search",
    # "15-single-pass-minmax",
    # "16-partitioning-minmax",
    # "17-merge-sort",
    # "18-quick-sort",

]

def get_base_filename(directory):
    for item in os.listdir(directory):
        if item.endswith(".py"):
            return os.path.splitext(item)[0]
    return os.path.basename(directory).split('-', 1)[-1]

def time_command(command, working_dir, shell=False, runs=1):
    """Runs a command multiple times and returns the minimum execution time in milliseconds."""
    timings = []
    for _ in range(runs):
        start_time = time.perf_counter()
        try:
            subprocess.run(
                command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                shell=shell, cwd=working_dir
            )
            end_time = time.perf_counter()
            timings.append((end_time - start_time) * 1000)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            cmd_str = ' '.join(command) if isinstance(command, list) else command
            print(f"  -> Error running '{cmd_str}' in '{working_dir}': {e}")
            return None
    return min(timings) if timings else None

def main():
    results = []
    exe_ext = ".exe" if sys.platform == "win32" else ""
    RUN_COUNT = 3  # Number of times to run each compiled program to get the best time

    print(f"Starting benchmark process (best of {RUN_COUNT} runs for compiled code)...")
    print("-" * 30)

    for directory in ALGORITHM_DIRS:
        if not os.path.isdir(directory):
            continue

        print(f"Processing: {directory}")
        base_name = get_base_filename(directory)
        
        py_file = os.path.join(directory, f"{base_name}.py")
        cpp_file = os.path.join(directory, f"{base_name}.cpp")
        rs_file = os.path.join(directory, f"{base_name}.rs")

        # --- Python Benchmark (single run is fine) ---
        if os.path.exists(py_file):
            command = ["python", f"{base_name}.py"]
            duration = time_command(command, working_dir=directory, runs=1)
            if duration is not None:
                results.append({"Algorithm": directory, "Language": "Python", "Time (ms)": duration})
                print(f"  -> Python: {duration:.4f} ms")

        # --- C++ Benchmark ---
        if os.path.exists(cpp_file):
            executable = f"{base_name}{exe_ext}"
            compile_command = ["g++", "-std=c++17", "-O2", f"{base_name}.cpp", "-o", executable, "-lstdc++"]
            print("  -> Compiling C++...")
            try:
                subprocess.run(compile_command, check=True, capture_output=True, text=True, cwd=directory)
                print(f"  -> Benchmarking C++ ({RUN_COUNT} runs)...")
                duration = time_command([f".\\{executable}" if sys.platform == "win32" else f"./{executable}"], working_dir=directory, shell=True, runs=RUN_COUNT)
                if duration is not None:
                    results.append({"Algorithm": directory, "Language": "C++", "Time (ms)": duration})
                    print(f"  -> C++ (best of {RUN_COUNT}): {duration:.4f} ms")
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                err_msg = e.stderr if hasattr(e, 'stderr') else e
                print(f"  -> C++ failed: {err_msg}")

        # --- Rust Benchmark ---
        if os.path.exists(rs_file):
            executable = f"{base_name}{exe_ext}"
            compile_command = ["rustc", f"{base_name}.rs", "-O", "-o", executable]
            print("  -> Compiling Rust...")
            try:
                subprocess.run(compile_command, check=True, capture_output=True, text=True, cwd=directory)
                print(f"  -> Benchmarking Rust ({RUN_COUNT} runs)...")
                duration = time_command([f".\\{executable}" if sys.platform == "win32" else f"./{executable}"], working_dir=directory, shell=True, runs=RUN_COUNT)
                if duration is not None:
                    results.append({"Algorithm": directory, "Language": "Rust", "Time (ms)": duration})
                    print(f"  -> Rust (best of {RUN_COUNT}): {duration:.4f} ms")
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                err_msg = e.stderr if hasattr(e, 'stderr') else e
                print(f"  -> Rust failed: {err_msg}")
        
        print("-" * 30)

    output_file = "benchmark_results.csv"
    print(f"Writing results to {output_file}...")
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Algorithm", "Language", "Time (ms)"])
        writer.writeheader()
        writer.writerows(results)

    print("Benchmarking complete!")

if __name__ == "__main__":
    main()