import json
import random

from mongoengine import *
from datetime import datetime

# Create your models here.
from utils.logger import logger


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
        queryset = queryset.order_by('-id')[:1][0]  # str
        if date is None:
            return json.dumps({"ret": queryset['ret'], "data": queryset['data']})
        date = date.split('%')[0]
        obj_data = json.loads(queryset['data'])  # obj
        globalDailyHistory = obj_data['globalDailyHistory']  #
        foreignList = obj_data['foreignList']  #
        countryAddConfirmRankList = obj_data['countryAddConfirmRankList']  #
        globalStatis = obj_data['globalStatis']  #
        continentStatis = obj_data['continentStatis']
        importStatis=obj_data['importStatis']
        TopList = importStatis['TopList']
        newGlobalDailyHistory = []
        newforeignList = []
        newcountryAddConfirmRankList = []
        newglobalStatis = {}
        newcontinentStatis = []
        newimportStatis={}
        newTopList = []
        step = (datetime.today().date() - datetime.strptime(date, "%Y-%m-%d").date()).days
        for i in TopList:
            item={}
            item['importedCase']= i['importedCase']-100*step if i['importedCase']-100*step>0 else random.randint(10,100)
            item['province']=i['province']
            newTopList.append(item)
        newimportStatis['TopList']=newTopList
        newglobalStatis['nowConfirm'] = globalStatis["nowConfirm"] - 1000 * step if globalStatis[
                                                                                        "nowConfirm"] - 1000 * step > 0 else random.randint(
            10000, 99999)
        newglobalStatis['confirm'] = globalStatis["confirm"] - 1000 * step if globalStatis[
                                                                                  "confirm"] - 1000 * step > 0 else random.randint(
            1000000, 9999999)
        newglobalStatis['heal'] = globalStatis["heal"] - 1000 * step if globalStatis[
                                                                            "heal"] - 1000 * step > 0 else random.randint(
            10000, 99999)
        newglobalStatis['dead'] = globalStatis["dead"] - 1000 * step if globalStatis[
                                                                            "dead"] - 1000 * step > 0 else random.randint(
            10000, 99999)
        newglobalStatis['nowConfirmAdd'] = globalStatis["nowConfirmAdd"] - 100000 * step if globalStatis[
                                                                                                "nowConfirmAdd"] - 100000 * step > 0 else random.randint(
            10000, 99999)
        newglobalStatis['confirmAdd'] = globalStatis["confirmAdd"] - 100000 * step if globalStatis[
                                                                                          "confirmAdd"] - 100000 * step > 0 else random.randint(
            10000, 99999)
        newglobalStatis['healAdd'] = globalStatis["healAdd"] - 100000 * step if globalStatis[
                                                                                    "healAdd"] - 100000 * step > 0 else random.randint(
            10000, 99999)
        newglobalStatis['deadAdd'] = globalStatis["deadAdd"] - 100000 * step if globalStatis[
                                                                                    "deadAdd"] - 100000 * step > 0 else random.randint(
            10000, 99999)

        for i in globalDailyHistory:
            month, day = i['date'].split('.')
            if datetime.strptime("-".join((i['y'], month, day)), "%Y-%m-%d") <= datetime.strptime(date, "%Y-%m-%d"):
                newGlobalDailyHistory.append(i)
        for i in foreignList:
            month, day = i['date'].split('.')
            if datetime.strptime("-".join((i['y'], month, day)), "%Y-%m-%d") <= datetime.strptime(date, "%Y-%m-%d"):
                newforeignList.append(i)
        for i in continentStatis:
            month, day = i['date'].split('/')
            if datetime.strptime("-".join(('2020', month, day)), "%Y-%m-%d") <= datetime.strptime(date, "%Y-%m-%d"):
                newcontinentStatis.append(i)
        for i in countryAddConfirmRankList:
            new_countryAddConfirmRank = {}
            num = i['addConfirm'] - 1000 * step
            new_countryAddConfirmRank['addConfirm'] = num if num > 0 else random.randint(1000, 9999)
            new_countryAddConfirmRank['nation'] = i['nation']
            newcountryAddConfirmRankList.append(new_countryAddConfirmRank)
            # print(new_countryAddConfirmRank)
        obj_data['globalDailyHistory'] = newGlobalDailyHistory
        obj_data['foreignList'] = newforeignList
        obj_data['countryAddConfirmRankList'] = newcountryAddConfirmRankList
        obj_data['globalStatis'] = newglobalStatis
        obj_data['continentStatis'] = newcontinentStatis
        obj_data['importStatis'] = newimportStatis
        new_data = json.dumps(obj_data)
        return json.dumps({"ret": queryset['ret'], "data": new_data})
