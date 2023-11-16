from database import db_connection

class Note:

    def __init__(self, user_id: int, title: str = "", description: str = ""):
        """
        Class Note.

        - Methods:
            - Save.
            - Show.
            - Delete.

        Args:
            user_id (int): User Id
            title (str): Note title.
            description (str): Description note.
        """
        self.user_id = user_id
        self.title = title
        self.description = description

    def save(self):

        connection, cursor = db_connection()
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s, NOW())"
        note = (self.user_id, self.title, self.description)
        try:
            cursor.execute(sql, note)
            connection.commit()
            return [cursor.rowcount, self]
        except Exception as e:
            print(f'Error: {type(e).__name__}')
        finally:
            cursor.close()
            connection.close()


    def show(self):

        connection, cursor = db_connection()
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f'Error: {type(e).__name__}')
        finally:
            cursor.close()
            connection.close()


    def delete(self, title: str):
        
        connection, cursor = db_connection()
        sql = 'DELETE FROM notes WHERE user_id = %s AND title LIKE %s'
        data = (self.user_id, title)
        try:
            cursor.execute(sql, data)
            connection.commit()
            return [cursor.rowcount, self]
        except Exception as e:
            print(f'Error: {type(e).__name__}')
        finally:
            cursor.close()
            connection.close()