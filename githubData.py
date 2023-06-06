import sqlite3
from github import Github
class GithubData:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        create table if not exists github_repos(
        id integer primary key,
        name text,
        access_level text,
        language text,
        stars integer,
        description text,
        update_date text
        )
        """)


    def add_repo(self, repos):
        self.cursor.execute("""
        insert into github_repos values(?, ?, ?, ?, ?, ?, ?)
        """, (self.get_id() + 1, repos.name, repos.access_level, repos.language, repos.stars, repos.description, repos.update_date))
        self.conn.commit()


    # read update delete
    def get_repo(self, id):
        self.cursor.execute("""
        select * from github_repos where id = ?
        """, (id,))
        row = self.cursor.fetchone()
        return Github(*row[1:])


    def get_all_repo(self):
        self.cursor.execute("""
        select * from github_repos
        """,)
        row = self.cursor.fetchall()
        return row


    def get_all_repo_language(self, language):
        self.cursor.execute("""
        select * from github_repos where language = ?
        """, (language,))
        row = self.cursor.fetchall()
        return row


    def delete_repo(self, id):
        self.cursor.execute("""
        delete * from github_repos where id = ?
        """, (id, ))
        self.conn.commit()


    def get_id(self):
        self.cursor.execute("""
        SELECT id from github_repos order by id desc limit 1""")
        row = self.cursor.fetchone()
        if row is None:
            return 0
        else:
            return row[0]