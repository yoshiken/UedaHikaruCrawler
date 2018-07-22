import os
import psycopg2
from get_eventernote import Event


def get_connection():
    dsn = 'postgresql://ueda:hikaru@localhost:5432/ueda'
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    return cur ,conn


def is_event(title):
    cur.execute('SELECT * FROM event WHERE title = %s',(title, ))
    rows = cur.fetchone()
    return bool(rows)

def insert_event(event):
    cur.execute('INSERT INTO event (day, title, location) VALUES (%s, %s, %s);', (event['date'], event['title'], event['location']))

def update_event(event):
    if event['doortime'] != '-':
        cur.execute('UPDATE event SET doortime = %s WHERE title = %s;', (event['doortime'], event['title']))
    if event['showtime'] != '-':
        cur.execute('UPDATE event SET showtime = %s WHERE title = %s;', (event['showtime'], event['title']))
    if event['closetime'] != '-':
        cur.execute('UPDATE event SET closetime = %s WHERE title = %s;', (event['closetime'], event['title']))

def event():
    Events = Event()
    eventList = Events.getEvents()
    for event in eventList:
        if not is_event(event['title']) :
            insert_event(event)
        update_event(event)
    conn.commit()

def is_news(news)

cur, conn = get_connection()
event()
cur.close()
conn.close()
