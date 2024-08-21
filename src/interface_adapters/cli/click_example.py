import click


@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.pass_context
def sub_command(ctx, name):
    """Sub command that greets the user."""
    click.echo(f'Hello, {name}!')


@click.command()
@click.pass_context
@click.option('--name', prompt='Your name', help='The person to greet.')
def main(ctx, name):
    """Main command that invokes the sub command."""
    click.echo('Welcome to the main command.')
    # Sub command로 이동
    ctx.invoke(sub_command, name=name)


if __name__ == '__main__':
    main()
