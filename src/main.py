from interface_adapters.cli import greeting_cli
from frameworks_drivers.db_setup import database_setup

def main():
    # 데이터베이스 설정
    database_setup.setup_database()
    # The central hub for starting the application.
    greeting_cli.greet()

if __name__ == '__main__':
    main()