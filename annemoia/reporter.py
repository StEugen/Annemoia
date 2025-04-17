import json
# TODO: Create report, take info from scanner
class Reporter:
    def __init__(self, findings=None):
        self.findings = findings or []

    def generate(self, fmt='json'):
        if fmt == 'json':
            with open('report.json', 'w') as f:
                json.dump(self.findings, f, indent=2)
        elif fmt == 'html':
            # TODO: produce an HTML report
            pass
        elif fmt == 'md':
            # TODO: produce md report 
            pass
