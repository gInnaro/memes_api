import psycopg2


class MemesDB:
    def __init__(self):
        self.conn = psycopg2.connect(user="postgres", password="143214", database="memes_db", host="memes-db-1", port="5432")
        self.cursor = self.conn.cursor()

    def create_db(self):
        self.cursor.execute("CREATE TABLE memes (id SERIAL PRIMARY KEY, name TEXT, url TEXT)")
        self.conn.commit()

    def unload_memes(self):
        self.cursor.execute("SELECT * FROM memes ORDER BY ID ASC")
        data = self.cursor.fetchall()
        return data

    def upload_memes(self, url: str, name):
        self.cursor.execute(f"INSERT INTO memes (url, name) VALUES (%s, %s)", (url, name))
        self.conn.commit()
        return True

    def one_memes(self, id: int):
        self.cursor.execute(f"SELECT name FROM memes WHERE id={id}")
        data = self.cursor.fetchone()
        if data != None:
            return data
        return False

    def update_memes(self, id: int, url, name):
        self.cursor.execute(f"SELECT * FROM memes WHERE id={id}")
        data = self.cursor.fetchone()
        if data != None:
            ids, names, urls = data
            if url:
                urls = url
            if name:
                names = name
            new_data = (names, urls)
            self.cursor.execute("UPDATE memes SET (url, name)=(%s, %s) WHERE id=%s", (urls, names, id))
            self.conn.commit()
            return new_data
        return False

    def delete_memes(self, id):
        self.cursor.execute(f"SELECT name FROM memes WHERE id={id} ORDER BY ID ASC")
        data = self.cursor.fetchone()
        if data != None:
            self.cursor.execute("DELETE FROM memes WHERE id=%s", (id,))
            self.conn.commit()
            return data
        return False

    def close(self):
        self.cursor.close()
        self.conn.close()


class AdminDB:
    def __init__(self):
        self.conn = psycopg2.connect(user="postgres", password="143214", database="memes_db", host="memes-db-1", port="5432")
        self.cursor = self.conn.cursor()

    def create_db(self):
        self.cursor.execute("CREATE TABLE admin_list (id SERIAL PRIMARY KEY, login VARCHAR(255), password VARCHAR(255))")
        self.conn.commit()

    def create_admin(self, username, password):
        self.cursor.execute(f"INSERT INTO admin_list (login, password) VALUES (%s, %s)", (username, password))
        self.conn.commit()

    def check_admin(self, username, password):
        self.cursor.execute(f"SELECT * FROM admin_list WHERE login = %s AND password=%s", (username, password))
        data = self.cursor.fetchone()
        if data != None:
            return True
        return False