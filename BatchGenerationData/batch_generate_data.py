import os

base_dir = os.path.abspath(os.path.dirname(__file__))
data_path = base_dir + "\data.txt"

with open(data_path, 'a+', encoding='utf-8') as f:
    for i in range(1, 101):
        real_name = 'test' + str(i)
        phone = str(15221739592 + i)
        email = 'test' + str(i) + '@mail.com'
        create_time = '2018-11-06 15:46:00'

        real_sql = "insert into sign_guest (realname, phone, email, sign, create_time, event_id) \
values ('" + real_name + "','" + phone + "','" + email + "',0,'" + create_time + "',1);"

        f.write(real_sql + '\n')

