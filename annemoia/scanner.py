import os

class Scanner:
    def __init__(self, root_path: str):
        self.root_path = root_path

    def run(self) -> list:
        # TODO: implement file discovery and vulnerability checks
        findings = []
        for dirpath, _, filenames in os.walk(self.root_path):
            for fname in filenames:
                if fname.endswith('.py'):
                    pass
        return findings
