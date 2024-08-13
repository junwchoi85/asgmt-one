import sqlite3
from frameworks_drivers.db.transaction_manager import TransactionManager

def setup_database():
    """
    Function to setup the database
    """
    connection = sqlite3.connect('mse800.db')
    print('Database connection established')
    transaction_manager = TransactionManager(connection)

    try:
        with transaction_manager as conn:
            c = conn.cursor()

            # Drop tables if they exist
            c.execute('DROP TABLE IF EXISTS user;')
            c.execute('DROP TABLE IF EXISTS role;')
            c.execute('DROP TABLE IF EXISTS user_role;')
            c.execute('DROP TABLE IF EXISTS car;')
            c.execute('DROP TABLE IF EXISTS booking;')
            print('Tables dropped')

            # Create tables
            c.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_code VARCHAR(6) NOT NULL,
                    username VARCHAR(45) NOT NULL,
                    password VARCHAR(45) NOT NULL,
                    UNIQUE (user_code)
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS role (
                    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role_code VARCHAR(6) NOT NULL,
                    desc VARCHAR(45)
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS user_role (
                    user_id INTEGER NOT NULL,
                    role_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
                    FOREIGN KEY (role_id) REFERENCES role (role_id) ON DELETE RESTRICT ON UPDATE RESTRICT
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS car (
                    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_code VARCHAR(6) NOT NULL,
                    make VARCHAR(45),
                    model VARCHAR(45),
                    year INTEGER,
                    mileage VARCHAR(45),
                    availability INTEGER,
                    UNIQUE (car_code)
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS booking (
                    bkg_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    bkg_code VARCHAR(6),
                    user_id INTEGER,
                    car_id INTEGER,
                    start_date VARCHAR(45),
                    end_date VARCHAR(45),
                    total_fee VARCHAR(45),
                    status VARCHAR(3),
                    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
                    FOREIGN KEY (car_id) REFERENCES car (car_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')
            print('Tables created')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    setup_database()