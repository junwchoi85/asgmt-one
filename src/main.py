from interface_adapters.cli import greeting_cli

def main():
    # The central hub for starting the application.
    greeting_cli.greet()

if __name__ == '__main__':
    main()