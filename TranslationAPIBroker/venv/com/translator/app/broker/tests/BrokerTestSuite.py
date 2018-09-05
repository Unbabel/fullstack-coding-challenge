import psycopg2
import unittest
from com.translator.app.broker.Broker import DB_Host
from com.translator.app.broker.Broker import DB_name
from com.translator.app.broker.Broker import DB_User
from com.translator.app.broker.Broker import DB_pass
from com.translator.app.broker.Broker import DB_port

class BrokerTestSuite (unittest.TestCase):


    def test_DBConnectivity(self):

        # Connect to the Postgre SQL server
        conn = None
        try:

            # Connect to the database
            print('Connecting to the Postgres SQL database...')
            conn = psycopg2.connect(host=DB_Host, database=DB_name, port=DB_port, user=DB_User, password=DB_pass);

            # Create a cursor
            cur = conn.cursor();

            # Execute a statement
            print('Getting Postgres database version...')
            cur.execute('SELECT version();')

            # Fetch the result
            db_version = cur.fetchone();
            print('DB version is: ')
            print(db_version)

            # Close the communication with PostgreSQL
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed')


if __name__ == '__main__':
    unittest.main();