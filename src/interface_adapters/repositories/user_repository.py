from entities.user import User

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def create(self, user: User) -> bool:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            INSERT INTO user (user_id, user_code, username, password)
            VALUES (?, ?, ?, ?)
            ''',
            (user.user_id, user.user_code, user.username, user.password))
        return cursor.lastrowid

        # deprecated. transaction will be managed by the transaction manager
        # try:
        #     # conn = get_connection()
        #     # c = conn.cursor()
        #     self.db_cursor.execute(
        #         '''
        #         INSERT INTO user (user_id, user_code, username, password)
        #         VALUES (?, ?, ?, ?)
        #         ''',
        #         (user.user_id, user.user_code, user.username, user.password))
        #     self.db_cursor.connection.commit()
        #     # conn.close()
        #     return True
        # except Exception as e:
        #     print(e)
        #     return False
    
    def get_last_user_code(self) -> str:
        """
        Get the last user code
        :return: User code
        """
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT user_code FROM user ORDER BY user_id DESC LIMIT 1
            ''')
        row = cursor.fetchone()
        # conn.close()
        return row[0] if row else None
    
    def get_by_username(self, username: str) -> User:
        """
        Get a user by username
        :param username: Username
        :return: User object
        """
        # conn = get_connection()
        # c = conn.cursor()
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM user WHERE username = ?
            ''',
            (username,))
        row = cursor.fetchone()
        # conn.close()
        return User(row[0], row[1], row[2], row[3]) if row else None

    def sign_in(self, username: str, password: str) -> User:
        """
        Sign in
        :param username: Username
        :param password: Password
        :return: True if successful, False otherwise
        """
        user = self.get_by_username(username)
        if user is None:
            return None
        if user.password == password :
            return user