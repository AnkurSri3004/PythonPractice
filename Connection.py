import mysql.connector
from mysql import connector



conn = mysql.connector.connect(host='127.0.0.1',database='insertdata',user='root',password='Ankur12345@')
cursor=conn.cursor()
# cursor.execute('select platform, app_version, count(distinct session_id) from bingo.')

# cursor.execute('select user_id from bingo_dev.b_user_coll_v2 where user_id =119175209588013 and city_id=331')
cursor.execute('SELECT * from insertdata.firstTable')
values=cursor.fetchall()
print(values)