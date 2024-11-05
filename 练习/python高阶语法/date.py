# import datetime
#
# date = datetime.date.today().strftime('%Y/%m/%d')
# now = str(date.today()).replace('/', '').replace('-', '')
# print(int(now))
# print(now)

import datetime
import pytz

# 获取当前的UTC时间
utc_now = datetime.datetime.utcnow()

# 使用pytz获取美国纽约时区
ny_timezone = pytz.timezone('America/New_York')

# 将UTC时间转换为纽约时区的当前时间
ny_now = utc_now.replace(tzinfo=pytz.utc).astimezone(ny_timezone)

# 输出美国当前的日期
print(ny_now.strftime('%Y-%m-%d'))


print(datetime.date.today())
pass