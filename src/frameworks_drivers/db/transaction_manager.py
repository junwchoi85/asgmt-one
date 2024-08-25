import sqlite3
from contextlib import contextmanager

from utils.logger import get_db_logger


class TransactionManager:
    def __init__(self, db_path: str):
        """
        Constructor for the transaction manager.

        Args:
            db_path (str): The path to the database file.
        """
        self.connection = sqlite3.connect(db_path)
        self.logger = get_db_logger()

    @contextmanager
    def transaction_scope(self):
        cursor = self.connection.cursor()
        try:
            yield cursor
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            self.connection.rollback()
            raise RuntimeError(f"Integrity error occurred: {e}")
        except sqlite3.OperationalError as e:
            self.connection.rollback()
            raise RuntimeError(f"Operational error occurred: {e}")
        except sqlite3.ProgrammingError as e:
            self.connection.rollback()
            raise RuntimeError(f"Programming error occurred: {e}")
        except sqlite3.Error as e:
            self.connection.rollback()
            raise RuntimeError(f"Error occurred: {e}")
        finally:
            cursor.close()

    def log_query(self, query, params):
        self.logger.debug(f"Executing query: {query} with params: {params}")

    def execute(self, cursor, query, params):
        self.log_query(query, params)
        cursor.execute(query, params)

    def close_connection(self):
        """
        Closes the connection to the database.

        This method closes the connection to the database that was established by the transaction manager.

        Parameters:
            None

        Returns:
            None
        """
        self.connection.close()

    def run_ddl(self, ddl):
        """
        Run a DDL statement.

        This method runs a DDL statement on the database.

        Parameters:
            ddl (str): The DDL statement to run.

        Returns:
            None
        """
        self.connection.execute(ddl)

    def run_dml(self, dml, values):
        """
        Run a DML statement.

        This method runs a DML statement on the database.

        Parameters:
            dml (str): The DML statement to run.
            values (tuple): The values to insert into the statement.

        Returns:
            None
        """
        self.connection.execute(dml, values)
