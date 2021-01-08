import json

from mongoengine import *
from datetime import datetime


# Create your models here.
class Info(Document):
    # poem
    meta = {
        # 数据库中显示的名字
        'collection': 'poem_data'
    }
    id = SequenceField(required=True, primary_key=True)
    ret = IntField()
    data = StringField()

    # 可以定义查询集
    @queryset_manager
    def show_newest(self, queryset, date):
        # 通过poem_id降序显示
        queryset = queryset.order_by('-id')[:1][0]#str
        obj_data = json.loads(queryset['data'])#obj
        globalDailyHistory = obj_data['globalDailyHistory']#
        newGlobalDailyHistory = []
        for i in globalDailyHistory:
            month, day = i['date'].split('.')
            if datetime.strptime("-".join((i['y'], month, day)), "%Y-%m-%d") <= datetime.strptime(date, "%Y-%m-%d"):
                newGlobalDailyHistory.append(i)
        obj_data['globalDailyHistory']=newGlobalDailyHistory
        new_data=json.dumps(obj_data)
        return json.dumps({"ret": queryset['ret'], "data": new_data})
