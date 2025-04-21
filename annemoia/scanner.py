from pathlib import Path
from typing import List, Dict

from annemoia.scanners.base import BaseScanner
from annemoia.scanners.python_scanner import PythonScanner
from annemoia.scanners.ruby_scanner import RubyScanner
# from annemoia.scanners.js_scanner import JavaScriptScanner

# TODO: Boot multiple scanners at once, if corresponding files found
class Scanner:
    def __init__(self, root_path: str, fity: str = "csv"):
        self.root = Path(root_path)

        self.scanners: List[BaseScanner] = [
            PythonScanner(),
            RubyScanner(self.root, fity),
        ]

        self._ext_map = {}
        for sc in self.scanners:
            for ext in sc.extensions():
                self._ext_map[ext] = sc

    def run(self) -> List[Dict]:
        findings: List[Dict] = []
        for fp in self.root.rglob('*'):
            if not fp.is_file():
                continue
            scanner = self._ext_map.get(fp.suffix)
            if not scanner:
                continue
            try:
                file_findings = scanner.analyze(fp)
                if file_findings:
                    for f in file_findings:
                        f.setdefault('file', str(fp))
                        findings.append(f)
            except Exception as e:
                findings.append({
                    'file': str(fp),
                    'error': str(e)
                })
        return findings
