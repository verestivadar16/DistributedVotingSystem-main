import mysql.connector

def sql_close_con(conn):
    conn.close()

def sql_open_con():
    dbhost = "localhost"
    dbuser = "aporka"
    dbpass = "nehezjelszo"
    db = "aporka"
    conn = None

    try:
        conn = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpass, database=db)
        print("Successfully connected to the database!")
    except mysql.connector.Error as error:
        print("Connect failed: {}".format(error))

    return conn

def sql_record_vote(voter_name, vote):
    conn = sql_open_con()

    sql = "INSERT INTO szavazatok(szavazoNeve, szavazat) VALUES (%s, %s)"
    values = (voter_name, vote)

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        print("Szavazat sikeresen rögzítve.")
    except Exception as e:
        print("Error:", str(e))

    sql_close_con(conn)

def sql_get_vote_by_voter(voter_name, question_id):
    conn = sql_open_con()

    sql = "SELECT szavazoNeve, valasz FROM szavazatok WHERE szavazoNeve = %s AND kerdes_id = %s"
    values = (voter_name, question_id, )

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()

        if result:
            return f"{result[0]}@{result[1]}"
        else:
            return "No vote found for the specified voter."
    except Exception as e:
        print("Error:", str(e))

    sql_close_con(conn)

def sql_post_new_client(username, email, password):
    conn = sql_open_con()
    sql = "INSERT INTO kliens(username, email, password, valasz_id) VALUES (%s, %s, %s, null)"
    values = (username, email, password)

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        print("New client created successfully in SQL")
    except Exception as e:
        print("Error:", str(e))

    sql_close_con(conn)

# GET
# KLIENS LEKÉRÉSE ID ALAPJÁN

def sql_get_client_by_id(id):
    conn = sql_open_con()

    sql = "SELECT id, username, email, password, valasz_id FROM kliens WHERE id = %s"
    values = (id,)

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()

        if result:
            ret = f"id: {result[0]} - username: {result[1]} - email: {result[2]} - password: {result[3]}"
        else:
            ret = "Client not found!"
    except Exception as e:
        print("Error:", str(e))

    sql_close_con(conn)
    return ret

# KLIENS LEKÉRÉSE EMAIL ALAPJÁN

def sql_get_client_by_email(email):
    conn = sql_open_con()

    sql = "SELECT id, username, email, password, valasz_id FROM kliens WHERE email LIKE %s"
    values = (email,)

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()

        if result:
            ret = f"id: {result[0]} - username: {result[1]} - email: {result[2]} - password: {result[3]}"
        else:
            ret = "Client not found!"
    except Exception as e:
        print("Error:", str(e))

    sql_close_con(conn)
    return ret

