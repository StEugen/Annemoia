import click
from annemoia.scanner import Scanner
#from annemoia.reporter import Reporter

@click.group()
def cli():
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
def hacker(path):
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--verbose', '-v', is_flag=True, help="Show detailed findings")
@click.option('--fity', '-ft', default='csv', help="File type used for report, by default csv is used ")
def scan(path, verbose, fity):
    scanner = Scanner(path, fity=fity)
    findings = scanner.run()
    click.echo(f"Found {len(findings)} potential issues.")
    if verbose and findings:
        click.echo()
        for idx, f in enumerate(findings, 1):
            file   = f.get('file', '<unknown>')
            line   = f.get('line', f.get('lineno', '?'))
            rule   = f.get('test_id', f.get('check_id', ''))
            msg    = f.get('issue_text', f.get('message', ''))
            click.echo(f"{idx}. {file}:{line} [{rule}] {msg}")

# Add format selection for brakeman and other scans
#@cli.command()
#@click.option('--format', 'fmt', type=click.Choice(['json', 'html']), default='json')
#def report(fmt):
#    reporter = Reporter()
#    reporter.generate(fmt)
#    click.echo(f"Report generated in report.{fmt}")

if __name__ == '__main__':
    cli()
