# -*- coding: utf8 -*-

import logging


#---------------------中文日志
logging.basicConfig(level=logging.WARNING, filemode='a', datefmt='"%Y/%m/%d/ %H:%M:%S "',
                    format='%(asctime)s -- %(message)s', )
encoding = "UTF-8"
handler = logging.FileHandler(filename='mylog.log', encoding='utf-8')
fmt = logging.Formatter(fmt='%(asctime)s -- %(message)s',datefmt='"%Y/%m/%d/ %H:%M:%S "')
handler.setFormatter(fmt)
logging.getLogger().addHandler(handler)

logging.error('测试')