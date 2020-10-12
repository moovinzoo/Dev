import cx_Oracle

# make dns
ip = '127.0.0.1'
port = 49161
SID = 'xe'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
con = cx_Oracle.connect('system', 'oracle', dsn_tns)
cur = con.cursor()

min_num_spam = 3

try:
    cur.execute("SELECT * from breakfast WHERE spam > {num}"\
                .format(num=min_num_spam))
    data = cur.fetchall() # Store in list of tuple

    for row in data:
        print(row)
    
    con.commit()

except:
    con.rollback()