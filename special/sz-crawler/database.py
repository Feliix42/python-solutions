import sqlite3 as sqlite


def database(entries):
    with sqlite.connect('awesome.db') as db:
        cursor = db.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Pages(
                url TEXT PRIMARY KEY,
                title TEXT
            );'''
        )

        for entry in entries:
            addentry(cursor, entry)


def addentry(cursor, entry):
    cmd = 'INSERT INTO Pages values(?, ?)'
    title = entry.title if entry.title is not None else 'Unknown'

    args = (entry.url, title)
    cursor.execute(cmd, args)


def listall():
    with sqlite.connect('awesome.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Pages')

        for row in cursor:
            url, title = row
            print('Title: {title}, URL: {url}'.format(title=title, url=url))
