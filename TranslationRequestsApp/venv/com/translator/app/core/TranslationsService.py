import psycopg2
import threading


from unbabel.api import UnbabelApi

# Module level constants (this maybe refactored to a shared configuration repo)
DB_Host = "localhost"
DB_name = "Test"
DB_User = "postgres"
DB_pass = "root"
DB_port = "5432"
UNBABEL_user = "fullstack-challenge"
UNBABEL_API_key = "9db71b322d43a6ac0f681784ebdcc6409bb83359"
UNBABEL_in_test_mode = True


class TranslationsService:

    # Locking mechanisms - One for each connection
    lock_queries = threading.Lock();
    lock_inserts = threading.Lock();

    # Two connections for better performance (simulating connection pool)
    select_conn = psycopg2.connect(host=DB_Host, database=DB_name, port=DB_port, user=DB_User, password=DB_pass)
    insert_conn = psycopg2.connect(host=DB_Host, database=DB_name, port=DB_port, user=DB_User, password=DB_pass)

    # Unbabel API instance
    uapi = UnbabelApi(UNBABEL_user, UNBABEL_API_key, sandbox=UNBABEL_in_test_mode)


    def submitRequest(self, submittedText):

        # Sync access to the shared connection
        TranslationsService.lock_inserts.acquire()
        cur = None
        try:
            cur = TranslationsService.insert_conn.cursor()
            cur.execute("INSERT INTO TRANSLATION (TXT) VALUES (%s)",[submittedText])
            TranslationsService.insert_conn.commit()

        except(Exception, psycopg2.DatabaseError ) as exception:

            print('Exception on submitRequest(...) on DB invocation... ')
            print(exception)
            raise exception

        finally:
            TranslationsService.lock_inserts.release()
            cur.close()


    def queryRequests(self):

        # Sync access to the shared connection
        TranslationsService.lock_queries.acquire()
        cur = None
        result = None
        try:

            cur = TranslationsService.select_conn.cursor()
            cur.execute("select trans_uid, txt, trans_result, state from (select trans_uid, txt, trans_result, state, character_length(trans_result) as len from translation order by len DESC NULLS LAST) as ordered")
            result = cur.fetchall()

        except(Exception, psycopg2.DatabaseError) as exception:
            print('Exception on queryRequests(...) ');
            print(exception);
            result = None
        finally:
            TranslationsService.lock_queries.release()
            cur.close()

        return result
