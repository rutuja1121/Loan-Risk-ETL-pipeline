
import subprocess
import sys

steps = [
    ("ETL profiling", "scripts/etl.py"),
    ("Data cleaning", "scripts/cleaning.py"),
    ("SQL analytics", "scripts/sql_analysis.py"),
]

for name, script in steps:
    print(f"\n{'=' * 50}")
    print(f"Running: {name}")
    print("=" * 50)

    result = subprocess.run(
        [sys.executable, script],
        check=False
    )

    if result.returncode != 0:
        print(f"\nPipeline stopped: {name} failed.")
        sys.exit(result.returncode)

print("\nPipeline completed successfully!")
