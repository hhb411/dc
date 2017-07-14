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
    elif (commodity == 'btc'):
        if (cycle == 'month'):
            result = KlineBtcMonth
        elif (cycle == 'week'):
            result = KlineBtcWeek
        elif (cycle == 'day'):
            result = KlineBtcDay
        elif (cycle == 'hour'):
            result = KlineBtcHour
        elif (cycle == 'min30'):
            result = KlineBtcMin30
        elif (cycle == 'min15'):
            result = KlineBtcMin15
        elif (cycle == 'min5'):
            result = KlineBtcMin5

    return result

#行情数据表：莱特币
class KlineLtcMonth(AbstractKline):
    time = models.CharField(primary_key=True, max_length=6)
    class Meta:
        db_table = 'data_ltc_month'

class KlineLtcWeek(AbstractKline):
    time = models.CharField(primary_key=True, max_length=8)
    class Meta:
        db_table = 'data_ltc_week'

class KlineLtcDay(AbstractKline):
    time = models.CharField(primary_key=True, max_length=8)
    class Meta:
        db_table = 'data_ltc_day'

class KlineLtcHour(AbstractKline):
    class Meta:
        db_table = 'data_ltc_hour'

class KlineLtcMin30(AbstractKline):
    class Meta:
        db_table = 'data_ltc_min30'

class KlineLtcMin15(AbstractKline):
    class Meta:
        db_table = 'data_ltc_min15'

class KlineLtcMin5(AbstractKline):
    class Meta:
        db_table = 'data_ltc_min5'

#行情数据表：比特币
class KlineBtcMonth(AbstractKline):
    time = models.CharField(primary_key=True, max_length=6)
    class Meta:
        db_table = 'data_btc_month'

class KlineBtcWeek(AbstractKline):
    time = models.CharField(primary_key=True, max_length=8)
    class Meta:
        db_table = 'data_btc_week'

class KlineBtcDay(AbstractKline):
    time = models.CharField(primary_key=True, max_length=8)
    class Meta:
        db_table = 'data_btc_day'

class KlineBtcHour(AbstractKline):
    class Meta:
        db_table = 'data_btc_hour'

class KlineBtcMin30(AbstractKline):
    class Meta:
        db_table = 'data_btc_min30'

class KlineBtcMin15(AbstractKline):
    class Meta:
        db_table = 'data_btc_min15'

#行情数据表：莱特币
class KlineBtcMin5(AbstractKline):
    class Meta:
        db_table = 'data_btc_min5'