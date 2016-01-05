import pymysql

conn = pymysql.connect(host='127.0.0.1',  # unix_socket='/tmp/mysql.sock',
                       user='JINH', passwd='initial1', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE breadmum_recipe")

user = 'test'
user_sql = '\"' + user + '\"'
date = '2015-12-24'
date_sql = '\"' + user + '\"'
created_date = '2015-12-24'
visited = 111
bookmarked = 222
name = ' 芝麻曲奇饼/饼干'
link = 'http://www.'

sql = "INSERT INTO `recipe` (`user`, `date`, `created_date`, `visited`, `bookmarked`, `name`, `link`) VALUES (" + user_sql + ", '2015-12-24', '2015-09-25', 34775, 2028, ' 芝麻曲奇饼/饼干', 'http://www.douguo.com/cookbook/10425823311.html')"
print(sql)
cur.execute(sql)
cur.connection.commit()
# print(cur.fetchone())
cur.close()
conn.close()
