import sqlite3

class ComicsDB:
    def __init__(self, filename):
        self.db = sqlite3.connect(filename)

    def put(self, id, title, alt, transcript, image_url):
        self.db.execute("insert into comics values (?, ?, ?, ?, ?)", (id, title, alt, transcript, image_url))
        self.db.commit()

    def get(self, id):
        return self.db.execute("select * from comics where id = ?", (id,)).fetchone()

    def getAlt(self, id):
        return self.db.execute("select alt from comics where id = ?",(id,)).fetchone()
    
    def getTitle(self, id):
        t1 = self.db.execute("select title from comics where id = ?",(id,)).fetchone()
        t2 = str(t1)
        t3 = t2[3:-3]
        return t3

    def get_all(self):
        cur = self.db.cursor()
        cur.execute("select * from comics")
        return cur.fetchall()
