import sqlite3

class TransactionManager:
    def __init__(self, connection):
        """
        Constructor for the transaction manager.

        Args:
            connection: The connection object to the database
        """
        self.connection = connection
    
    def transaction_scope(self):
        """
        Returns the connection object for the transaction scope.

        :return: The connection object for the transaction scope.
        """
        return self.connection
    
    def __enter__(self):
        """
        Enter method for the transaction manager.

        Returns:
            connection: The connection object for the transaction.
        """
        self.connection.execute('BEGIN')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the transaction manager context.

        Args:
            exc_type: The type of the exception raised, if any.
            exc_val: The exception instance raised, if any.
            exc_tb: The traceback of the exception raised, if any.
        """
        if exc_type is not None:
            self.connection.execute('ROLLBACK')
        else:
            self.connection.execute('COMMIT')

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