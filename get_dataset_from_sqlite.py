import pymysql
import traceback
import os
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info(" connect with Mysql......")
db = pymysql.connect(host='139.9.113.51', port=3306, user='chatbot', password='chatbot', db='chatbot', charset='utf8')
cursor = db.cursor()

try:
    cursor.execute('SELECT * from Corpus')
    result = cursor.fetchall()
except:
    info = sys.exc_info()
    logger.info(info[0], ':', info[1])
    db.rollback()
finally:
    cursor.close()
    conn.close()
logger.info(" close Mysql.")
'''
couplet_path = '/root/Couplet/couplet/temp/'
couplet_ups = list()
couplet_downs = list()

for value in result:
    couplet_ups.append(' '.join([i for i in value[1]])+'\n')
    couplet_downs.append(' '.join([i for i in value[2]])+'\n')

with open(os.path.join(couplet_path, 'in.txt'), 'w') as f:
    f.writelines(couplet_ups)
with open(os.path.join(couplet_path, 'out.txt'), 'w') as f:
    f.writelines(couplet_downs)
'''
logger.info(" save train data in {}.".format(couplet_path))