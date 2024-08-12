import sqlite3

class TransactionManager:
    def __init__(self, connection):
        self.connection = self.transaction_scope()
    
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
    