# import psycopg2
import cx_Oracle

def PythonDatabaseExample(userid, passwd):
    try:
        # make dns
        ip = '127.0.0.1'
        port = 49161
        SID = 'xe'
        dsn_tns = cx_Oracle.makedsn(ip, port, SID)
        con = cx_Oracle.connect('system', 'oracle', dsn_tns)
        cur = con.cursor()

        # conn = psycopg2.connect(host="db.yale.edu", port=5432, dbname="univdb", user=userid, password=passwd)
        conn = psycopg2.connect('system/oracle@')
        cur = conn.cursor()
        try:
            cur.execute("insert into instructor values(%s, %s, %s, %s)", ("77987", "Kim", "Physics", 98000))
            conn.commit()
        except Exception as sqle:
            print("Could not insert tuple. ", sqle)
            conn.rollback()
        cur.execute(("select dept_name, avg (salary) " "from instructor group by dept_name"))
        for dept in cur:
            print(dept[0], dept[1])
    except Exception as sqle:
        print("Exception : ", sqle)




PythonDatabaseExample("admin", "0000")