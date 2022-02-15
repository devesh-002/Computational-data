import twint
import datetime
import nest_asyncio

def convertToDateTime(string):
    dateTimeList = string.split()
    ListLength = len(dateTimeList)
    if ListLength == 2:
        return string
    if ListLength == 1:
        return string + " 00:00:00"
    else:
        return ""

nest_asyncio.apply()
c = twint.Config()
c.Search = "#covid"
c.Since = "2021-06-01 00:00:00"
c.Until = "2021-06-30 00:00:00"
datetime.datetime.strptime(convertToDateTime(), "%Y-%m-%d %H:%M:%S")
c.Store_csv = True
c.Output = "test.csv"
twint.run.Search(c)