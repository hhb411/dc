from django.db import models
import json

#所有行情数据表的抽象类
class AbstractKline(models.Model):
    class Meta:
        abstract = True
    time = models.CharField(primary_key=True, max_length=12)
    open = models.FloatField()
    close = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    amount = models.IntegerField() #成交量
    count = models.IntegerField() #成交笔数
    vol = models.FloatField() #成交额
    #转成json map
    def toJSON(self):
        return json.dumps(
            dict(
                [(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]
            )
        )

    #转成数组
    def toArr(self):
        arr = [self.time, self.open, self.close, self.low, self.high, self.amount, self.count, self.vol]
        return arr

# 返回model
# commodity: 交易品种(ltc, btc...)
# cycle: 周期（day, hour...）
def getModel(commodity, cycle):
    if (commodity == 'ltc'):
        if (cycle == 'month'):
            result = KlineLtcMonth
        elif (cycle == 'week'):
            result = KlineLtcWeek
        elif (cycle == 'day'):
            result = KlineLtcDay
        elif (cycle == 'hour'):
            result = KlineLtcHour
        elif (cycle == 'min30'):
            result = KlineLtcMin30
        elif (cycle == 'min15'):
            result = KlineLtcMin15
        elif (cycle == 'min5'):
            result = KlineLtcMin5
    return result

class KlineLtcMonth(AbstractKline):
    class Meta:
        db_table = 'data_ltc_month'

class KlineLtcWeek(AbstractKline):
    class Meta:
        db_table = 'data_ltc_week'

#行情数据表：莱特币-日数据
class KlineLtcDay(AbstractKline):
    class Meta:
        db_table = 'data_ltc_day'

#行情数据表：莱特币-小时数据
class KlineLtcHour(AbstractKline):
    class Meta:
        db_table = 'data_ltc_hour'

#行情数据表：莱特币
class KlineLtcMin30(AbstractKline):
    class Meta:
        db_table = 'data_ltc_min30'

#行情数据表：莱特币
class KlineLtcMin15(AbstractKline):
    class Meta:
        db_table = 'data_ltc_min15'

#行情数据表：莱特币
class KlineLtcMin5(AbstractKline):
    class Meta:
        db_table = 'data_ltc_min5'
