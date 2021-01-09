# 国外
# https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryMerge
# 国内
# https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
import json

import requests

from coivd.utils.logger import logger

r = json.loads(requests.get("https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign").text)

b = requests.post("http://8.135.59.30/coivd_info", data=r)

logger.info(b.text)
print(b.text)
