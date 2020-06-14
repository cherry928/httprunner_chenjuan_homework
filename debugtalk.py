import random
from identity import IdNumber

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


if __name__ == "__main__":
    # print(get_random_mobilephone())
    # print(get_random_id(3))
    print(get_str_random())