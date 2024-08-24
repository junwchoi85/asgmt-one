import sqlite3
from frameworks_drivers.db.transaction_manager import TransactionManager
from random import choice, randint


def setup_database(transaction_manager: TransactionManager):
    """
    Function to setup the database
    """
    print('Database connection established')

    try:
        with transaction_manager.transaction_scope() as c:
            # Drop tables if they exist
            c.execute('DROP TABLE IF EXISTS customer;')
            c.execute('DROP TABLE IF EXISTS user;')
            c.execute('DROP TABLE IF EXISTS role;')
            c.execute('DROP TABLE IF EXISTS user_role;')
            c.execute('DROP TABLE IF EXISTS car;')
            c.execute('DROP TABLE IF EXISTS car_detail;')
            c.execute('DROP TABLE IF EXISTS car_rental_terms;')
            c.execute('DROP TABLE IF EXISTS booking;')
            c.execute('DROP TABLE IF EXISTS promotion;')

            print('*Tables dropped\n')

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
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(45) NULL,
                    UNIQUE (cst_code),
                    UNIQUE (username)
                );
            ''')
            # Create indexes
            c.execute(
                'CREATE UNIQUE INDEX IF NOT EXISTS user_code_UNIQUE ON customer (cst_code)')
            c.execute(
                'CREATE UNIQUE INDEX IF NOT EXISTS username_UNIQUE ON customer (username)')

            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_customer_updated_at
                AFTER UPDATE ON customer
                FOR EACH ROW
                BEGIN
                    UPDATE customer SET updated_at = CURRENT_TIMESTAMP WHERE cst_id = OLD.cst_id;
                END;
            ''')
            print('*** customer Table created')

            # User
            c.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_code VARCHAR(7) NOT NULL,
                    username VARCHAR(45) NOT NULL,
                    password VARCHAR(45) NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL,
                    UNIQUE (user_code),
                    UNIQUE (username)
                );
            ''')
            # Create indexes
            c.execute(
                'CREATE UNIQUE INDEX IF NOT EXISTS user_code_UNIQUE ON user (user_code)')
            c.execute(
                'CREATE UNIQUE INDEX IF NOT EXISTS username_UNIQUE ON user (username)')
            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_user_updated_at
                AFTER UPDATE ON user
                FOR EACH ROW
                BEGIN
                    UPDATE user SET updated_at = CURRENT_TIMESTAMP WHERE user_id = OLD.user_id;
                END;
            ''')
            print('*** user Table created')

            # Role
            c.execute('''
                CREATE TABLE IF NOT EXISTS role (
                    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role_code VARCHAR(7) NOT NULL,
                    desc TEXT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL,
                    UNIQUE (role_code)
                );
            ''')
            # Create indexes for role table
            c.execute(
                'CREATE UNIQUE INDEX IF NOT EXISTS role_code_UNIQUE ON role (role_code)')
            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_role_updated_at
                AFTER UPDATE ON role
                FOR EACH ROW
                BEGIN
                    UPDATE role SET updated_at = CURRENT_TIMESTAMP WHERE role_id = OLD.role_id;
                END;
            ''')
            print('*** role Table created')

            # user_role
            c.execute('''
                CREATE TABLE IF NOT EXISTS user_role (
                    uro_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    desc TEXT NULL,
                    user_id INT NULL,
                    role_id INT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
                    FOREIGN KEY (role_id) REFERENCES role (role_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')
            # Create indexes for user_role table
            c.execute(
                'CREATE INDEX IF NOT EXISTS uro_role_idx ON user_role (role_id)')
            c.execute(
                'CREATE INDEX IF NOT EXISTS uro_user_idx ON user_role (user_id)')

            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_user_role_updated_at
                AFTER UPDATE ON user_role
                FOR EACH ROW
                BEGIN
                    UPDATE user_role SET updated_at = CURRENT_TIMESTAMP WHERE uro_id = OLD.uro_id;
                END;
            ''')
            print('*** user_role Table created')

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
                    status VARCHAR(10) NOT NULL DEFAULT 'ACTIVE',
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL,
                    UNIQUE (car_code)
                );
            ''')
            # Create indexes
            c.execute(
                'CREATE UNIQUE INDEX IF NOT EXISTS car_code_UNIQUE ON car (car_code)')
            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_car_updated_at
                AFTER UPDATE ON car
                FOR EACH ROW
                BEGIN
                    UPDATE car SET updated_at = CURRENT_TIMESTAMP WHERE car_id = OLD.car_id;
                END;
            ''')
            print('*** car Table created')

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
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (car_id) REFERENCES car (car_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')
            # Create indexes for car_detail table
            c.execute(
                'CREATE INDEX IF NOT EXISTS car_id_idx ON car_detail (car_id)')
            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_car_detail_updated_at
                AFTER UPDATE ON car_detail
                FOR EACH ROW
                BEGIN
                    UPDATE car_detail SET updated_at = CURRENT_TIMESTAMP WHERE car_dtl_id = OLD.car_dtl_id;
                END;
            ''')
            print('*** car_detail Table created')

            # Create car_rental_terms table
            c.execute('''
                CREATE TABLE IF NOT EXISTS car_rental_terms (
                    car_rtr_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_id INT NULL,
                    min_rent_period INT NULL,
                    max_rent_period INT NULL,
                    price_per_day DECIMAL(10,2) NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (car_id) REFERENCES car (car_code) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')

            # Create indexes for car_rental_terms table
            c.execute(
                'CREATE INDEX IF NOT EXISTS foriegnKey_car_id_idx ON car_rental_terms (car_id)')

            # Create trigger to update updated_at column for car_rental_terms table
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_car_rental_terms_updated_at
                AFTER UPDATE ON car_rental_terms
                FOR EACH ROW
                BEGIN
                    UPDATE car_rental_terms SET updated_at = CURRENT_TIMESTAMP WHERE car_rtr_id = OLD.car_rtr_id;
                END;
            ''')
            print('*** car_rental_terms Table created')

            # Create promotion table
            c.execute('''
                CREATE TABLE IF NOT EXISTS promotion (
                    prm_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    desc TEXT NULL,
                    discount_rate DECIMAL(2,2) NULL,
                    dt_start DATETIME NULL,
                    dt_end DATETIME NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL
                );
            ''')
            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_promotion_updated_at
                AFTER UPDATE ON promotion
                FOR EACH ROW
                BEGIN
                    UPDATE promotion SET updated_at = CURRENT_TIMESTAMP WHERE prm_id = OLD.prm_id;
                END;
            ''')
            print('*** promotion Table created')

            # Create car_promotion table
            c.execute('''
                CREATE TABLE IF NOT EXISTS car_promotion (
                    cpr_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_rtr_id INTEGER NULL,
                    prm_id INTEGER NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by VARCHAR(7) NOT NULL DEFAULT 'system',
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (prm_id) REFERENCES promotion (prm_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
                    FOREIGN KEY (car_rtr_id) REFERENCES car_rental_terms (car_rtr_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')

            # Create indexes
            c.execute(
                'CREATE INDEX IF NOT EXISTS cpr_promotion_idx ON car_promotion (prm_id)')
            c.execute(
                'CREATE INDEX IF NOT EXISTS cpr_rtr_idx ON car_promotion (car_rtr_id)')

            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_car_promotion_updated_at
                AFTER UPDATE ON car_promotion
                FOR EACH ROW
                BEGIN
                    UPDATE car_promotion SET updated_at = CURRENT_TIMESTAMP WHERE cpr_id = OLD.cpr_id;
                END;
            ''')
            print('*** car_promotion Table created')

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
                    updated_at TIMESTAMP NULL,
                    updated_by VARCHAR(7) NULL,
                    FOREIGN KEY (cst_id) REFERENCES customer (cst_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
                    FOREIGN KEY (car_dtl_id) REFERENCES car_detail (car_dtl_id) ON DELETE NO ACTION ON UPDATE NO ACTION
                );
            ''')
            # 인덱스 생성
            c.execute('CREATE INDEX IF NOT EXISTS cst_id_idx ON booking (cst_id)')
            c.execute(
                'CREATE INDEX IF NOT EXISTS car_dtl_id_idx ON booking (car_dtl_id)')
            # Create trigger to update updated_at column
            c.execute('''
                CREATE TRIGGER IF NOT EXISTS update_booking_updated_at
                AFTER UPDATE ON booking
                FOR EACH ROW
                BEGIN
                    UPDATE booking SET updated_at = CURRENT_TIMESTAMP WHERE booking_id = OLD.booking_id;
                END;
            ''')
            print('*** booking Table created')

            print('Tables created')

            # Insert data
            # insert admin user
            c.execute('''
                INSERT INTO user (user_code, username, password, created_by)
                VALUES ('sup-001', 'admin', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'system')
                ''')
            # insert admin role
            c.execute('''
                INSERT INTO role (role_code, desc, created_by)
                VALUES ('admin', 'Administrator', 'system')
                ''')
            # insert user role
            c.execute('''
                INSERT INTO user_role (desc, user_id, role_id, created_by)
                VALUES ('Admin role for admin user', 1, 1, 'system')
                ''')

            # run web scraping to get car data
            # insert car data
            # Car data to be inserted
            car_data = [
                ('car-002', 'Toyota Corolla / Similar', '2019 - 2023',
                 5, 'Auto', 1, 2, '1800cc', '6.1L / 100km', 'ACTIVE'),
                ('car-003', 'Hyundai Elantra / Similar', '2018 - 2019',
                 5, 'Auto', 2, 3, '1800cc', '6.4L / 100km', 'ACTIVE'),
                ('car-004', 'Mitsubishi ASX 2WD / Similar', '2019 - 2022',
                 5, 'Auto', 2, 3, '2000cc', '7.6L / 100km', 'ACTIVE'),
                ('car-005', 'Nissan Xtrail AWD / Similar', '2019 - 2022',
                 5, 'Auto', 4, 3, '2500cc', '9.6L / 100km', 'ACTIVE'),
                ('car-006', 'Nissan X Trail 2WD / Similar', '2019 - 2022',
                 5, 'Auto', 4, 3, '2500cc', '9.6L / 100km', 'ACTIVE'),
                ('car-007', 'Hyundai Santa Fe AWD / Similar', '2019 - 2022',
                 5, 'Auto', 4, 3, '2500cc +', '10.6L / 100km', 'ACTIVE'),
                ('car-008', 'Hyundai iMax / Similar', '2019',
                 8, 'Auto', 3, 4, '2400cc', '9.5L / 100km', 'ACTIVE'),
                ('car-009', 'Toyota HiAce / Similar', '2016 - 2017',
                 12, 'Auto', 8, 8, '3000cc', '9.2L / 100km', 'ACTIVE'),
                ('car-010', 'Mitsubishi Triton 4WD', '2021 - 2022',
                 5, 'Auto', 3, 2, '2400cc', '9.8L / 100km', 'ACTIVE'),
                ('car-011', 'Hyundai Staria', '2020 - 2022', 2, 'Auto',
                 '4.9 cubic meter cargo', 0, '2200cc', '8.2L / 100km', 'ACTIVE')
            ]

            # Insert car data into the database
            for car in car_data:
                c.execute('''
                    INSERT INTO car (car_code, name, year, passenger, transmission, luggage_large, luggage_small, engine, fuel, status, created_by)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'system')
                    ''', car)

            # Car detail data to be inserted
            # Assuming these are the car IDs from the car table
            car_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            colors = ['Red', 'Blue', 'Green', 'Black', 'White',
                      'Silver', 'Gray', 'Yellow', 'Orange', 'Purple']
            statuses = ['Available', 'Maintenance', 'Reserved']

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

            # Car rental terms data to be inserted
            car_rental_terms_data = [
                (1, 1, 5, 41.99),
                (2, 1, 5, 43.96),
                (3, 1, 5, 42.96),
                (4, 1, 5, 61.02),
                (5, 1, 5, 42.96),
                (6, 1, 5, 70.64),
                (7, 1, 5, 138.26),
                (8, 1, 5, 143.54),
                (9, 1, 5, 52.64),
                (10, 1, 5, 57.96)
            ]

            # Insert car rental terms data into the database
            for car_rental_terms in car_rental_terms_data:
                c.execute('''
                    INSERT INTO car_rental_terms (car_id, min_rent_period, max_rent_period, price_per_day, created_by)
                    VALUES (?, ?, ?, ?, 'system')
                    ''', car_rental_terms)
            print('Data inserted')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # transaction_manager.close_connection()
        print('Database connection closed')


if __name__ == "__main__":
    transaction_manager = TransactionManager('mse800.db')
    setup_database(transaction_manager)
