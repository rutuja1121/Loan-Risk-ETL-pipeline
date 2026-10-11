
import subprocess
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

steps = [
    ("ETL profiling", "scripts/etl.py"),
    ("Data cleaning", "scripts/cleaning.py"),
    ("SQL analytics", "scripts/sql_analysis.py"),
    ("PySpark transformation", "scripts/spark_transform.py"),
]

# Avoid conflicts with a separately installed Spark version.
env = os.environ.copy()
env.pop("SPARK_HOME", None)

for name, script in steps:
    print(f"\n{'=' * 50}", flush=True)
    print(f"Running: {name}", flush=True)
    print("=" * 50, flush=True)

    result = subprocess.run(
        [sys.executable, os.path.join(PROJECT_ROOT, script)],
        cwd=PROJECT_ROOT,
        env=env,
        check=False,
    )

    if result.returncode != 0:
        print(f"\nPipeline stopped: {name} failed.", flush=True)
        sys.exit(result.returncode)

print("\nAll pipeline stages completed successfully!", flush=True)
