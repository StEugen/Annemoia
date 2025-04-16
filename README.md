# Annemoia
Annemoia is an open source DevSecOps tool designed to analyze codebases for potential vulnerabilities and run security tests that emulate how attackers might exploit weaknesses. Built in Python 3, Annemoia aims to empower developers and security teams by automating vulnerability analysis, providing actionable insights, and integrating seamlessly into CI/CD pipelines.

Note: This project is still in development.

## Features
- Code Vulnerability Analysis: Scans source code for known vulnerabilities and insecure coding practices.

- Security Testing Suite: Runs tests to simulate various hacker attack scenarios.

- Command-Line Interface (CLI): A simple and intuitive CLI tool (ann) for quick scanning and reporting.

- Extensible: Plugin architecture and modular design make it easy to add new security tests and integrations.

- Reporting: Generates detailed reports with actionable recommendations to improve code security.



## Installation
Clone the repository and install the package along with its dependencies:

```bash
git clone https://github.com/yourusername/annemoia.git
cd annemoia
pip install -r requirements.txt
```

## Usage
Annemoia provides a command-line interface (CLI) named ann to start vulnerability scans and security tests.

Basic Scan
To perform a basic code scan on your project:
```bash
ann scan /path/to/your/code
```

Running Specific Tests
To run a specific set of tests (e.g., SQL injection checks, XSS, etc.):
```bash
ann test --type sql-injection /path/to/your/code
```

Generating Reports
After scanning, you can generate a detailed report. By default, the report is saved as annemoia_report.json in the current working directory:
```bash
ann report --format json
```
Help and Options
For a list of available commands and options:

```bash
ann --help
Example help output:

Usage: ann [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  scan      Scan the provided codebase for vulnerabilities.
  test      Run specific security tests.
  report    Generate a vulnerability report.
```

## Configuration
Annemoia uses a configuration file (e.g., annemoia.yml) to customize its behavior. You can configure:

Scan rules: Activate or deactivate certain vulnerability rules.

Test sets: Specify which tests to run by default.

Reporting options: Customize the report format (MD, HTML, etc.) and output location.

Exclusions: Define files or directories to exclude from scanning.

Sample configuration file in YAML:
```yaml
scan:
  rules:
    - id: 'SQL001'
      enabled: true
    - id: 'XSS002'
      enabled: true
report:
  format: json
  output: './annemoia_report.md'
exclude:
  - 'tests/'
  - 'docs/'
```

## Integration with CI/CD
Integrating Annemoia into your CI/CD pipeline can help catch vulnerabilities early. For example, in a GitHub Actions workflow, you can use:

```yaml
name: CI Security Scan

on:
  push:
    branches:
      - main

jobs:
  security_scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install annemoia
      - name: Run Annemoia Scan
        run: ann scan .
```
This workflow ensures that security scans are performed on every push to the main branch.
