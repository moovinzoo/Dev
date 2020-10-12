import cx_Oracle

# make dns
ip = '127.0.0.1'
port = 49161
SID = 'xe'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
con = cx_Oracle.connect('system', 'oracle', dsn_tns)
cur = con.cursor()

# # Create new table 'breakfast'
# cur.execute("CREATE TABLE breakfast(\
#                 name VARCHAR(32),\
#                 spam INT,\
#                 eggs INT,\
#                 sausage INT,\
#                 PRIMARY KEY (name))")

# If query is valid(executed), commit.
try:
    cur.execute("INSERT INTO breakfast(name, spam, eggs, sausage) VALUES('Spam and sausage Plate', 5, 1, 7)")
    con.commit()

# If failed, rollback.
except:
    con.rollback()

print("num of inserted row: %d", cur.rowcount)
con.close()