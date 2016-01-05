import pymysql

conn = pymysql.connect(host='127.0.0.1',  # unix_socket='/tmp/mysql.sock',
                       user='JINH', passwd='initial1', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE breadmum_recipe")

user = 'test'
user_sql = '\"' + user + '\"'
date = '2015-12-27'
date_sql = '\"' + date + '\"'
created_date = '2015-12-25'
created_date_sql = '\"' + created_date + '\"'
visited = 999
bookmarked = 888
name = ' 芝麻曲奇饼/饼干'
name_sql = '\"' + name + '\"'
link = 'testall'
link_sql = '\"' + link + '\"'

sql = "REPLACE INTO `recipe` (`user`, `date`, `created_date`, `visited`, `bookmarked`, `name`, `link`) VALUES (" + user_sql + ", " + date_sql + ", " + created_date_sql + ", " + str(
    visited) + ", " + str(bookmarked) + ", " + name_sql + ", " + link_sql + ")"
print(sql)
cur.execute(sql)
cur.connection.commit()
# print(cur.fetchone())
cur.close()
conn.close()
