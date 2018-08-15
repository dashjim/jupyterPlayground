# coding=UTF-8

import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='0.0.0.0', database='ivr_rec', user='root')
df = pd.read_sql('select * from flow', con=db_connection)

df = df.drop(labels='id', axis=1)

# To Chinese
menu_values = ['0001', '1010', '1020', '1030', '1040', '1210', '1220', '1230', '1240']
menu_meaning = ['欢迎词', '延迟还款业务', '账单分期业务', '分期优惠活动', '其它', '查询密码重置', '交易密码重置', '修改交易密码', '其它']
df['menu'] = df['menu'].replace(menu_values, menu_meaning)

usr_op_values = ['balance', 'audit', 'userPasswordWrong']
usr_op_meaning = ['查询余额', '查询账单', '密码错误']
df['app_operation_end'] = df['app_operation_end'].replace(usr_op_values, usr_op_meaning)

is_hit_value = ['hit', 'miss']
is_hit_meaning = ['命中', '未命中']
df['target']=df['target'].replace(is_hit_value, is_hit_meaning)

df.rename(index=str, columns={"app_operation_end": "source", 'menu': 'intend'}, inplace=True)

df.to_csv('app_behavior_02.csv', index=False)
