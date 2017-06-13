# [WARNING] All of directorys must end with "/" !

import logging
import src.model

########
# Pixiv account & password
PIXIV_ID = "----------"
PIXIV_PW = "----------"

# Directory to save log files.
LOG_DIR = 'log/'

# Directory includes data-set.
DATA_DIR = 'dataset/'

# Directory to save image from crawler.py
CRAWLER_DIR = 'pixiv/'


########
# Log's output level. Choose "NOTSET", "DEBUG", "INFO", "WARNING", "ERROR" and "CRITICAL".
LOG_LEVEL = logging.INFO

# If you want to print log to console, set it True. (And log will still be write into log files.)
TO_CONSOLE = True


########
# Training (Just for training.)
GPU = True
SAVE_MODEL = False
AUGMENT_RATE = 0.7
ADAM_RATE = 0.00005

# Don't change this.
MODEL = src.model.CNN_02
SIZE = 133

# Demo Creator
CREATE_DEMO = False
DEMO_ROOT = '/home/shin-u16/document/html_nginx/'
PAGE_DIR = 'pixiv/'
PAGE_TEMPLATE = 'src/template.html'

