import json

from mongoengine import *


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
    def show_newest(self, queryset):
        # 通过poem_id降序显示
        queryset = queryset.order_by('-id')[:1][0]
        return json.dumps({"ret": queryset['ret'], "data": queryset['data']})
