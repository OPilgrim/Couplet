# 获取数据集
import sqlite3
import os
couplet_path = '/root/Couplet/couplet/train/'

conn = sqlite3.connect('')   # 请输入数据库文件
cursor = conn.cursor()

couplet_ups = list()
couplet_downs = list()

cursor.execute('select * from Couplet_warehouse')
for value in cursor.fetchall():
    couplet_up.append(' '.join([i for i in value[1]])+'\n')
    couplet_down.append(' '.join([i for i in value[2]])+'\n')

cursor.close()
conn.close()

with open(os.path.join(couplet_path, 'in.txt'), 'w') as f:
    f.writelines(couplet_ups)
with open(os.path.join(couplet_path, 'out.txt'), 'w') as f:
    f.writelines(couplet_downs)