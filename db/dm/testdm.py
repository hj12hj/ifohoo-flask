import dmPython

try:
    conn = dmPython.connect(user='firmGNCW', password='888888888', server='10.55.255.101',  port=5236)
    cursor  = conn.cursor()
    # cursor.execute("create table test(id int,name varchar(20))")
    # insert date
    # cursor.execute("insert into test(id,name) values(1,'chinese')")
    # cursor.execute("insert into test(id,name) values(2,'math')")
    # update data
    # cursor.execute("update test set name=\'English\' where name = \'chinese\'")
    cursor.execute("select * from test")
    res = cursor.fetchall()
    print(res)
    print('python: conn success!')
    conn.close()
except (dmPython.Error, Exception) as err:
    print(err)
