# coding=UTF-8

import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='0.0.0.0', database='ivr_rec', user='root')
# db_connection = sql.connect(host='192.168.43.240', database='avaya_demo', user='root', password='123456')
df = pd.read_sql('select * from flow', con=db_connection)
db_connection.commit()


df = df.drop(labels='id', axis=1)

# To Chinese
menu_values = ['0001',   '1010',       '1011',   '1020',       '1021',   '1030',       '1031',        '1040', '1210',      '1211',        '1220',       '1221',       '1230',      '1231',      '1240', '1050',      '1060']
menu_meaning = ['欢迎词', '延迟还款业务', '延迟还款', '账单分期业务', '账单分期', '分期优惠活动', '分期优惠活动_', '其它', '查询密码重置', '查询密码重置_', '交易密码重置', '交易密码重置_','修改交易密码', '修改交易密码_','其它',  '贷款办理',   '开卡']
df['menu'] = df['menu'].replace(menu_values, menu_meaning)

usr_op_values = ['balance', 'audit', 'userPasswordWrong']
usr_op_meaning = ['查询余额', '查询账单', '密码错误']
df['app_operation_end'] = df['app_operation_end'].replace(usr_op_values, usr_op_meaning)

is_hit_value = ['hit', 'miss']
is_hit_meaning = ['命中', '未命中']
df['target']=df['target'].replace(is_hit_value, is_hit_meaning)

df.rename(index=str, columns={"app_operation_end": "source", 'menu': 'intend'}, inplace=True)

df.to_csv('app_behavior_02.csv', index=False)

db_connection.close()
