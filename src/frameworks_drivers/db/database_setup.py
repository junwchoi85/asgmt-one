import sqlite3
from frameworks_drivers.db.transaction_manager import TransactionManager
from random import choice, randint


def setup_database(transaction_manager: TransactionManager):
    """
    Function to setup the database
    """
    print('Database connection established')

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
            # Customer
            c.execute('''
                CREATE TABLE IF NOT EXISTS customer (
                    cst_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cst_code VARCHAR(7) NOT NULL,
                    username VARCHAR(45) NOT NULL,
                    password VARCHAR(45) NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(45) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_by VARCHAR(45) NULL,
                    UNIQUE (cst_code),
                    UNIQUE (username)
                );
            ''')

            # User
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

            # Role
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

            # User Role
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

            # Car
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

            # Car Detail
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

            # Car Rental Terms
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

            # Booking
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

            # Insert data
            # insert admin user
            c.execute('''
                INSERT INTO user (user_code, username, password, created_by)
                VALUES ('sup-001', 'admin', 'admin', 'system')
                ''')
            # insert admin role
            c.execute('''
                INSERT INTO role (role_code, desc, created_by)
                VALUES ('admin', 'Administrator', 'system')
                ''')
            # insert user role
            c.execute('''
                INSERT INTO user_role (user_id, role_id, created_by)
                VALUES (1, 1, 'system')
                ''')

            # run web scraping to get car data
            # insert car data
            # Car data to be inserted
            car_data = [
                ('car-002', 'Toyota Corolla / Similar', '2019 - 2023',
                 5, 'Auto', 1, 2, '1800cc', '6.1L / 100km'),
                ('car-003', 'Hyundai Elantra / Similar', '2018 - 2019',
                 5, 'Auto', 2, 3, '1800cc', '6.4L / 100km'),
                ('car-004', 'Mitsubishi ASX 2WD / Similar', '2019 - 2022',
                 5, 'Auto', 2, 3, '2000cc', '7.6L / 100km'),
                ('car-005', 'Nissan Xtrail AWD / Similar', '2019 - 2022',
                 5, 'Auto', 4, 3, '2500cc', '9.6L / 100km'),
                ('car-006', 'Nissan X Trail 2WD / Similar', '2019 - 2022',
                 5, 'Auto', 4, 3, '2500cc', '9.6L / 100km'),
                ('car-007', 'Hyundai Santa Fe AWD / Similar', '2019 - 2022',
                 5, 'Auto', 4, 3, '2500cc +', '10.6L / 100km'),
                ('car-008', 'Hyundai iMax / Similar', '2019',
                 8, 'Auto', 3, 4, '2400cc', '9.5L / 100km'),
                ('car-009', 'Toyota HiAce / Similar', '2016 - 2017',
                 12, 'Auto', 8, 8, '3000cc', '9.2L / 100km'),
                ('car-010', 'Mitsubishi Triton 4WD', '2021 - 2022',
                 5, 'Auto', 3, 2, '2400cc', '9.8L / 100km'),
                ('car-011', 'Hyundai Staria', '2020 - 2022', 2, 'Auto',
                 '4.9 cubic meter cargo', 0, '2200cc', '8.2L / 100km')
            ]

            # Insert car data into the database
            for car in car_data:
                c.execute('''
                    INSERT INTO car (car_code, name, year, passenger, transmission, luggage_large, luggage_small, engine, fuel, created_by)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'system')
                    ''', car)

            # Car detail data to be inserted
            # Assuming these are the car IDs from the car table
            car_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            colors = ['Red', 'Blue', 'Green', 'Black', 'White',
                      'Silver', 'Gray', 'Yellow', 'Orange', 'Purple']
            statuses = ['Available', 'Sold', 'Maintenance', 'Reserved']

            car_detail_data = []
            car_detail_id = 1

            for car_id in car_ids:
                for _ in range(10):
                    # Random mileage between 1000 and 100000 km
                    mileage = f"{randint(1000, 100000)} km"
                    color = choice(colors)
                    vin = f"VIN{randint(100000, 999999)}"  # Random VIN number
                    status = choice(statuses)
                    car_detail_data.append(
                        (car_detail_id, car_id, mileage, color, vin, status))
                    car_detail_id += 1

            # Insert car detail data into the database
            for car_detail in car_detail_data:
                c.execute('''
                    INSERT INTO car_detail (car_dtl_id, car_id, mileage, color, vin, status, created_by)
                    VALUES (?, ?, ?, ?, ?, ?, 'system')
                    ''', car_detail)

            print('Data inserted')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # transaction_manager.close_connection()
        print('Database connection closed')


if __name__ == "__main__":
    transaction_manager = TransactionManager('mse800.db')
    setup_database(transaction_manager)
