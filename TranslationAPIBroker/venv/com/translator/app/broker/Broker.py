import psycopg2
from unbabel.api import UnbabelApi
import json
import time

# Declare module constants (this maybe refactored to a shared configuration repo)
DB_Host = "localhost"
DB_name = "Test"
DB_User = "postgres"
DB_pass = "root"
DB_port = "5432"
DB_Translation_selection_qry = "SELECT ID, TRANS_UID, TXT FROM TRANSLATION WHERE STATE != 'completed'"
DB_Translation_update_translation_stmt = "UPDATE TRANSLATION SET STATE = %s, TRANS_RESULT = %s WHERE ID = %s"
DB_Translation_update_state_stmt = "UPDATE TRANSLATION SET STATE = %s, TRANS_UID = %s  WHERE ID = %s"
UNBABEL_user = "fullstack-challenge"
UNBABEL_API_key = "9db71b322d43a6ac0f681784ebdcc6409bb83359"
UNBABEL_in_test_mode = True


def main():

    # Start
    print('## Start of Broker() ##')

    try:
        
        # 2) Prepare the Unbabel API usage
        uapi = UnbabelApi(UNBABEL_user, UNBABEL_API_key, sandbox=UNBABEL_in_test_mode)

        # 3) Generate a DB connection
        conn_select = psycopg2.connect(host=DB_Host, database=DB_name, port=DB_port, user=DB_User, password=DB_pass)
        conn_update = psycopg2.connect(host=DB_Host, database=DB_name, port=DB_port, user=DB_User, password=DB_pass)

        # 4) Select all translation requests in non-complete status
        print('Executing fetch of submitted translations...')
        cur = conn_select.cursor()

        if cur is not None:
            cur.execute(DB_Translation_selection_qry)

            # 4) For each Translation Request
            # 4.1) - Call /translation/:uid/
            # 4.2) - update database request
            for id, uid, txt in cur.fetchall():

                cur_update = conn_update.cursor()

                # Query and issue API request
                translatedText = None
                status = None
                print('Fetching the status of request id : ' + str(id))
                print('id is:' + str(id))
                print('uid is:' + str(uid))
                print('txt is:' + str(txt))
                
                if uid is not None:

                    # Query the translation status
                    translation = uapi.get_translation(uid)

                    # Parse the status response
                    if translation is not None:
                        print('Translation request data: ')
                        print(translation)
                        status = translation.status
                        translatedText = translation.translation
                    else:
                        print('No Translation Status Retrieve response in call to Unbabel API...')
                        continue
                else:
                    # Post a new translation
                    translation_resp = uapi.post_translations(text=txt, source_language="en", target_language="es")

                    # Parse the Request submission response
                    if translation_resp is not None:
                        print('Submitted Request Reply: ' + str(translation_resp))
                        uid = translation_resp.uid
                        status = translation_resp.status
                        print('Request UID: ' + str(uid))
                    else:
                        print('No Translation Submission request-response received in call to Unbabel API...')
                        continue

                print('Request submitted to SandBoxAPI')

                # Update the status on the database
                if cur_update is not None:
                    if translatedText is not None and len(translatedText) != 0:
                        print('Updating request with translated text')
                        result = cur_update.execute( DB_Translation_update_translation_stmt, (status,translatedText,id))
                        conn_update.commit()
                    else :
                        if uid is not None:
                            print('Updating request with uid')
                            cur_update.execute(DB_Translation_update_state_stmt, (status, uid, id))
                            conn_update.commit()
                        else:
                            print('Translation UID is null. Cannot update the database')
                else:
                    print('DB UPDATE cursor is null...')

                cur_update.close()

            cur.close();
        else:
            print('DB SELECT cursor is null...')


    except(Exception,psycopg2.DatabaseError ) as error:
        print('Exception...  ')
        print(error)

    finally:
        if conn_select is not None:
            conn_select.close()
            print('Database SELECT connection closed.')

        if conn_update is not None:
            conn_update.close()
            print('Database UPDATE connection closed.')

        # Sleep for 2 seconds
        time.sleep(2)

    # END
    print('## End of Broker() ##')


if __name__ == '__main__':
    while True:
        main()



