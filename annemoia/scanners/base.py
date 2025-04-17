from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict

class BaseScanner(ABC):
    """
    All language scanners should inherit from this.
    """
    @abstractmethod
    def extensions(self) -> List[str]:
        """File extensions this scanner handles, e.g. ['.py']"""
        ...

    @abstractmethod
    def analyze(self, file_path: Path) -> List[Dict]:
        """Return a list of findings (dicts) for a single file."""
        ...

