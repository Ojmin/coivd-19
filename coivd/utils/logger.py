import logging

LOG_PATH = r'C:\Users\admin\Desktop\coivd-19\coivd\new.log'
# LOG_PATH = '/home/log'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=LOG_PATH, filemode='a')
logger = logging.getLogger(__name__)
