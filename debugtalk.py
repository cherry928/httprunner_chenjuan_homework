import random
from identity import IdNumber
import pymysql

# 生成随机手机号码
def get_random_mobilephone(count=1):
    phone_list = []
    for i in range(count):
        start_phone = random.choice(['133','149','153','173','177','180','181','189','199','130','131','132',
                                     '145','155','156','166','171','175','176','185','186','166','135','136',
                                     '137','138','139','147','150','151','152','157','158','159','172','178',
                                     '182','183','184','187','188','198'])
        end_phone = ''.join(random.sample('0123456789', 8))
        phone_list.append(start_phone + end_phone)
    return phone_list

# 生成随机身份证号码
def get_random_id(count=1):
    random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
    return IdNumber.generate_id(random_sex, count)  # 随机生成身份证号

# 生成一个指定长度的随机字符串
def get_str_random(randomlength=8, count=1):
    str_list = []
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopkrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(count):
        ran_str = ''
        for i in range(randomlength):
            ran_str += base_str[random.randint(0,length)]
        str_list.append(ran_str)
    return str_list

# 中文乱码问题解决
def to_iso8859(t):
    return t.encode("utf8").decode("iso8859-1")

def to_utf_8(t):
    return t.encode("iso8859-1").decode("utf8")

# 操作数据库
def connect_database():
    connect = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='12345678',
        database='autotest'
    )
    return connect

# 查询数据
def get_database_data():
    connect = connect_database()
    cur = connect.cursor()
    cur.execute('select * from %s;'%'test01')
    all_data = cur.fetchall()
    connect.close()
    return all_data

# 插入数据
def insert_into_database(id,exp,atc):
    connect = connect_database()
    cur = connect.cursor()
    cur.execute('insert into %(base)s(id,expect_value,actual_value) values("%(id)d", "%(expect_value)s", "%(actual_value)s");'
                %dict(base='test01',id=id,expect_value=exp,actual_value=atc))
    connect.commit()
    cur.close()
    connect.close()

# 改数据
def update_database(id,atc):
    con = connect_database()
    cur = con.cursor()
    cur.execute("update %(base)s set actual_value='%(atc)s' where id=%(id)d;" % dict(base='test01',atc=atc,id=id))
    con.commit()
    cur.close()
    con.close()

# 删数据
def delete_database(id):
    con = connect_database()
    cur = con.cursor()
    cur.execute("delete from %(base)s where id=%(id)d;" % dict(base='test01',id=id))
    con.commit()
    cur.close()
    con.close()

if __name__ == "__main__":
    # print(get_random_mobilephone())
    # print(get_random_id(3))
    # print(get_str_random())
    # insert_into_database(7,'快乐大本营','快乐大本营04')
    # print(get_database_data())
    # update_database(8,'快乐大本营001')
    delete_database(8)