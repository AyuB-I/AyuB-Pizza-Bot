import sqlite3


class SQLighter:
    def __init__(self, database_file):
        """ Подключаемся к базе данных """
        self.connection = sqlite3.connect(database=database_file)
        self.cursor = self.connection.cursor()

    def get_users(self, status=True):
        """ Получаем активных пользователей """
        with self.connection:
            return self.cursor.execute("SELECT * FROM users WHERE status = ?", (status,)).fetchall()

    def add_user(self, user_id, user_name, full_name, status=True):
        """ Добавляем пользователя в БД """
        with self.connection:
            return self.cursor.execute("INSERT INTO users(user_id, user_name, full_name, status) \
            VALUES (?, ?, ?, ?)", (user_id, user_name, full_name, status))

    def add_phone_number(self, user_id, phone_number):
        """ Добавляем номер телефона в БД """
        return self.cursor.execute("UPDATE users SET phone_number = ? WHERE user_id = ?", (phone_number, user_id))

    def update_status(self, user_id, status):
        """ Обновляем статус подписки """
        return self.cursor.execute("UPDATE users SET status = ? WHERE user_id = ?", (status, user_id))

    def user_exists(self, user_id):
        """ Проверяем существует ли такой пользователь в БД """
        result = self.cursor.execute(f"SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
        return bool(len(result))

    def close(self):
        """ Закрываем соединение с БД """
        self.connection.close()
