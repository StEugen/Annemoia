import subprocess
import json
from pathlib import Path
from typing import List, Dict
from .base import BaseScanner

class PythonScanner(BaseScanner):
    def extensions(self) -> List[str]:
        return ['.py']

    def analyze(self, file_path: Path) -> List[Dict]:
        result = subprocess.run(
            ['bandit', '-f', 'json', '-q', str(file_path)],
            capture_output=True,
            text=True,
            check=False
        )
        if not result.stdout:
            return []
        data = json.loads(result.stdout)
        return data.get("results", [])

