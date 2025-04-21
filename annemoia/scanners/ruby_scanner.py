import subprocess
from pathlib import Path
from datetime import datetime
from typing import List
from .base import BaseScanner

class RubyScanner(BaseScanner):
    def __init__(self, root_path: Path, fity: str = 'csv'):
        self.root = root_path
        self._ran = False
        self.fity = fity

    def extensions(self) -> List[str]:
        return ['.rb']

    def analyze(self, file_path: Path) -> None:
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        report_file = f"brakeman_report_{timestamp}.{self.fity}"
        report_path = self.root / report_file
        # Stupid afk move.... ig....
        if self._ran:
            return
        self._ran = True

        try:
            print("Detected Ruby, using brakeman for scan.")
            subprocess.run(
                ['brakeman','-o', str(report_path)],
                cwd=str(self.root),
                check=True
            )
            print(f"Report saved at {report_path}")
        except subprocess.CalledProcessError as e:
            print(f"Brakeman error (exit {e.returncode}): {e.stderr.strip()}")
