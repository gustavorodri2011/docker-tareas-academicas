import os, time, psycopg2
while True:
    try:
        psycopg2.connect(os.getenv('DATABASE_URL'))
        break
    except:
        time.sleep(1)
