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
            c.execute('DROP TABLE IF EXISTS customer;')
            c.execute('DROP TABLE IF EXISTS user;')
            c.execute('DROP TABLE IF EXISTS role;')
            c.execute('DROP TABLE IF EXISTS user_role;')
            c.execute('DROP TABLE IF EXISTS car;')
            c.execute('DROP TABLE IF EXISTS car_detail;')
            c.execute('DROP TABLE IF EXISTS car_rental_terms;')
            c.execute('DROP TABLE IF EXISTS booking;')
            print('Tables dropped')

            # Create tables
            c.execute('''
                CREATE TABLE IF NOT EXISTS customer (
                    cst_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cst_code VARCHAR(7) NOT NULL,
                    username VARCHAR(45) NOT NULL,
                    password VARCHAR(45) NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(45) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(45) NOT NULL,
                    UNIQUE (cst_code),
                    UNIQUE (username)
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_code VARCHAR(7) NOT NULL,
                    username VARCHAR(45) NOT NULL,
                    password VARCHAR(45) NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(7) NULL,
                    UNIQUE (user_code),
                    UNIQUE (username)
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS role (
                    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role_code VARCHAR(7) NOT NULL,
                    desc TEXT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(7) NULL
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS user_role (
                    user_id INTEGER NOT NULL,
                    role_id INTEGER NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
                    FOREIGN KEY (role_id) REFERENCES role (role_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS car (
                    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_code VARCHAR(45) NOT NULL,
                    name VARCHAR(45) NOT NULL,
                    year VARCHAR(45) NOT NULL,
                    passenger INTEGER NOT NULL,
                    transmission VARCHAR(6) NOT NULL,
                    luggage_large INTEGER NOT NULL,
                    luggage_small INTEGER NOT NULL,
                    engine VARCHAR(45) NOT NULL,
                    fuel VARCHAR(45) NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(7) NULL,
                    UNIQUE (car_code)
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS car_detail (
                    car_dtl_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_id INTEGER NOT NULL,
                    mileage VARCHAR(45) NULL,
                    color VARCHAR(45) NULL,
                    vin VARCHAR(45) NULL,
                    status VARCHAR(45) NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (car_id) REFERENCES car (car_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS car_rental_terms (
                    car_rtr_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_dtl_id INTEGER NOT NULL,
                    promotion VARCHAR(45) NULL,
                    min_rent_period INTEGER NULL,
                    max_rent_period INTEGER NULL,
                    rental_price FLOAT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (car_dtl_id) REFERENCES car_detail (car_dtl_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')

            c.execute('''
                CREATE TABLE IF NOT EXISTS booking (
                    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cst_id INTEGER NOT NULL,
                    car_dtl_id INTEGER NOT NULL,
                    start_date DATETIME NULL,
                    end_date DATETIME NULL,
                    total_fee FLOAT NULL,
                    status VARCHAR(45) NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (cst_id) REFERENCES customer (cst_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
                    FOREIGN KEY (car_dtl_id) REFERENCES car_detail (car_dtl_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')

            print('Tables created')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()
        print('Database connection closed')

if __name__ == "__main__":
    setup_database()