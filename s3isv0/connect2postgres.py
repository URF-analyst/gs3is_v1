# Note: the module name is psycopg, not psycopg3
import psycopg

# Connect to an existing database
with psycopg.connect("postgres://koyeb-adm:BvmbDo65hTEG@ep-steep-sound-a2zhajww.eu-central-1.pg.koyeb.app/koyebdb") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute the SQL command to create the extension
        cur.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
        # Commit the transaction
    conn.commit()
    cur.close()
conn.close()

