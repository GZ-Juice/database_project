import django
import xlrd
from dateutil import parser
from _datetime import datetime
import re

def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False

django.setup()
from TestModel.models import Bike,CyclingRecords


# Bike.objects.create(BikeId='1990',CompanyName='mobike',BikeState=1,LocationX=120.123,LocationY=50.046,Battery=99,ServiceLife=3)
date = "2019-9-12 9:12:36"
date = parser.parse(date)
# print(type(date))
# print(date)
# bike = Bike.objects.get(BikeId='1990')
# CyclingRecords.objects.create(BikeId=bike,UserId='154',LocationX=180.234,LocationY=65.123,StartTime=date,EndTime=date)



# start = datetime.strptime('9/30/2017 8:42:50','%m/%d/%Y %H:%M:%S')
# end = datetime.strptime('9/30/2017 10:42:50','%m/%d/%Y %H:%M:%S')
# cycrecord = CyclingRecords(UserId='135',StartTime=start,EndTime=end,LocationX=100.563,LocationY=120.142)
# cycrecord.BikeId = bike
# cycrecord.save()

# CyclingRecords.objects.get(id=1).delete()
# workbook = xlrd.open_workbook("G:\\作业\\数据库\\test.xlsx")
# # name = workbook.sheet_names()
# # print(name)
# #
# # worksheet = workbook.sheet_by_name("Bike")
# # print(worksheet)
# # nrows = worksheet.nrows
# # for i in range(1,nrows):
# #     print(worksheet.row_values(i))
# #
# # print("cell:",worksheet.cell_value(1,1))