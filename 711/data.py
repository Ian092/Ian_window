from dotenv import load_dotenv # type: ignore
import psycopg2 # type: ignore
import os
load_dotenv()



def get_areas() -> list[tuple]:
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql ='''
            SELECT DISTINCT sarea
            FROM youbike;
            '''

            cursor.execute(sql)
            return cursor.fetchall()
    conn.close()