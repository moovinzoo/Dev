import cx_Oracle

# make dns
ip = '127.0.0.1'
port = 49161
SID = 'xe'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
con = cx_Oracle.connect('system', 'oracle', dsn_tns)
cur = con.cursor()

try:
    cur.execute("select * from v$version")
    con.commit()
except:
    con.rollback()
con.close()