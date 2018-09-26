# -*- coding: utf8 -*-

import logging


#---------------------中文日志
import logging
logging.basicConfig(level=logging.WARNING, filemode='a', datefmt='"%Y/%m/%d/ %H:%M:%S "',
                    format='%(asctime)s -- %(message)s', )
encoding = "UTF-8"
handler = logging.FileHandler(filename='mylog.log', encoding='utf-8')
fmt = logging.Formatter(fmt='%(asctime)s -- %(message)s', datefmt='"%Y/%m/%d/ %H:%M:%S "')
handler.setFormatter(fmt)
grid_log = logging.getLogger('grid_log')
grid_log.addHandler(handler)
grid_log.error('测试')