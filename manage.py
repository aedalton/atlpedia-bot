import click

from atlpedia_bot import create_app


@click.group()
def cli():
    pass

@click.command()
def initdb():
    from atlpedia_bot.models import init_db

    init_db()
    click.echo('Initialized the database')


@click.command()
def run():
    app = create_app()
    app.run()


cli.add_command(initdb)
cli.add_command(run)


if __name__ == '__main__':
    cli()
