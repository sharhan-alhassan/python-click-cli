import click

@click.group()
def cli():
    pass


@cli.command(help=' --name (Add name)')
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    "command: cooltool"
    click.echo(f"Hello, {name}")