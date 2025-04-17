import click
from annemoia.scanner import Scanner
from annemoia.reporter import Reporter

@click.group()
def cli():
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
def hacker(path):
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
def scan(path):
    scanner = Scanner(path)
    findings = scanner.run()
    click.echo(f"Found {len(findings)} potential issues.")

@cli.command()
@click.option('--format', 'fmt', type=click.Choice(['json', 'html']), default='json')
def report(fmt):
    reporter = Reporter()
    reporter.generate(fmt)
    click.echo(f"Report generated in report.{fmt}")

if __name__ == '__main__':
    cli()
