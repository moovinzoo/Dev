import cx_Oracle

# make dns
ip = '127.0.0.1'
port = 49161
SID = 'xe'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
con = cx_Oracle.connect('system', 'oracle', dsn_tns)

# con = cx_Oracle.connect('system/oracle@127.0.0.1/xe')
# con = cx_Oracle.connect('system/oracle@192.168.0.1/xe')
cur = con.cursor()
cur.execute("CREATE TABLE breakfast(\
                name VARCHAR(32),\
                spam INT,\
                eggs INT,\
                sausage INT,\
                PRIMARY KEY (name))")
con.close()