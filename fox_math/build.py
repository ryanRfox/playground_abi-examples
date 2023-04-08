# Build the sample contract in this directory using Beaker and output to ./artifacts
from pathlib import Path

import select_math
import calculator

def build_select_math() -> Path:
    """Build the beaker app, export it to disk, and return the Path to the app spec file"""
    app_spec = select_math.app.build()
    output_dir = Path(__file__).parent / "select_math-artifacts"
    print(f"Dumping {app_spec.contract.name} to {output_dir}")
    app_spec.export(output_dir)
    return output_dir / "application.json"

def build_calculator() -> Path:
    """Build the beaker app, export it to disk, and return the Path to the app spec file"""
    app_spec = calculator.app.build()
    output_dir = Path(__file__).parent / "calculator-artifacts"
    print(f"Dumping {app_spec.contract.name} to {output_dir}")
    app_spec.export(output_dir)
    return output_dir / "application.json"


if __name__ == "__main__":
    build_select_math()
    build_calculator()
