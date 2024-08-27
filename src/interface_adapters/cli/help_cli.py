from interface_adapters.cli.cli import Cli


def view_help(cli: Cli):
    cli.echo(
        """
        ============== Help Menu ==============
         1. Sign In: Log in to your account.
         2. Sign Up: Create a new account.
         3. Exit: Close the application.
         4. Help: Show this help menu.
         5. Admin: Access admin functionalities.
        =======================================
        """
    )
    cli.pause()
    return
