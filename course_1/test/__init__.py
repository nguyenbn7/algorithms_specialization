from pathlib import Path
from sys import path

# Resolve for parent module
current_path = Path(__file__).parent.resolve()
path.append(current_path.parent.resolve().as_posix())
