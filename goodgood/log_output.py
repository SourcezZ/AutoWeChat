import logging
from datetime import datetime
import os
lgTime = datetime.now().strftime('%m%d')

logger = logging.Logger(__name__)
logger.setLevel(level = logging.INFO)

if not os.path.isdir('logFile'):
    print('新的应用日志文件夹logFile')
    os.makedirs('logFile')

handler = logging.FileHandler('logFile/' + lgTime + '.txt',encoding='utf-8')
handler.setLevel = (logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)

def ptLg(str1):
    logger.info(str1)
