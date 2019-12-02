import django
import os
import xlrd
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Config.settings')
django.setup()
from TestModel.models import Bike
from TestModel.models import Center
from TestModel.models import CyclingRecords
from TestModel.models import RepairRecords
from TestModel.models import CompanyInfo
from TestModel.models import IllegalParking


"""
bike = Bike(
    BikeId="000003",
    CompanyName="MOBike",
    BikeState=True,
    LocationX=121.348,
    LocationY=34.389,
    Battery=50,
    ServiceLife=4
)
if bike.save_if_valid():
    print("Yes!")
else:
    print(bike._errors)
"""


workbook = xlrd.open_workbook("G:\\Python Project\\database_project\\data.xlsx")
worksheet = workbook.sheet_by_index(1)
nrows = worksheet.nrows
ncols = worksheet.ncols
print("行数：", nrows, "列数：", ncols)

# 插入第一张表

worksheet = workbook.sheet_by_name("Bike")
nrows = worksheet.nrows
ncols = worksheet.ncols
print("行数：", nrows, "列数：", ncols)
for i in range(nrows):
    if i != 0:
        InputInfo = worksheet.row_values(i)
        print(InputInfo)
        t = datetime.strptime(InputInfo[5], '%Y-%m-%d')  # 字符串转时间格式
        t = t.strftime('%Y-%m-%d')
        BId = str(int(InputInfo[0]))
        CN = InputInfo[1]
        BS = InputInfo[2]
        LX = InputInfo[3]
        LY = InputInfo[4]
        LT = t
        BT = InputInfo[6]
        SL = InputInfo[7]
        bike = Bike(
            BikeId=BId,
            CompanyName=CN,
            BikeState=BS,
            LocationX=LX,
            LocationY=LY,
            LaunchTime=t,
            Battery=BT,
            ServiceLife=SL
        )
        if bike.save_if_valid():
            print("Yes!")
        else:
            print(bike._errors)


# 插入第二张表

worksheet = workbook.sheet_by_name("CyclingRecords")
nrows = worksheet.nrows
ncols = worksheet.ncols
print("行数：", nrows, "列数：", ncols)
for i in range(nrows):
    if i != 0:
        InputInfo = worksheet.row_values(i)
        print(InputInfo)
        bike = Bike.objects.get(BikeId=int(InputInfo[0]))
        dt = InputInfo[2]
        st = dt + ' ' + str(InputInfo[3])
        st = datetime.strptime(st, '%Y-%m-%d %H:%M:%S')
        et = dt + ' ' + str(InputInfo[4])
        et = datetime.strptime(et, '%Y-%m-%d %H:%M:%S')
        CR = CyclingRecords(
            BikeId=bike,
            UserId=str(int(InputInfo[1])),
            StartTime=st,
            EndTime=et,
            LocationX=InputInfo[5],
            LocationY=InputInfo[6]
        )
        if CR.save_if_valid():
            print("Yes!")
        else:
            print(CR._errors)


# 插入第三张表

# 插入第三张表
worksheet = workbook.sheet_by_name("Center")
nrows = worksheet.nrows
ncols = worksheet.ncols
print("行数：", nrows, "列数：", ncols)
for i in range(nrows):
    if i != 0:
        InputInfo = worksheet.row_values(i)
        print(InputInfo)
        CId = InputInfo[0]
        LX = InputInfo[1]
        LY = InputInfo[2]
        BN = InputInfo[3]
        WN = InputInfo[4]
        PN = InputInfo[5]
        SN = InputInfo[6]
        QRN = InputInfo[7]
        LN = InputInfo[8]
        CN = InputInfo[9]
        center = Center(
            CenterId=CId,
            LocationX=LX,
            LocationY=LY,
            BrakeNum=BN,
            WheelNum=WN,
            PedalNum=PN,
            SaddleNum=SN,
            QRcodeNum=QRN,
            LockNum=LN,
            ChainNum=CN
        )
        if center.save_if_valid():
            print("Yes!")
        else:
            print(center._errors)


# 插入第四张表

worksheet = workbook.sheet_by_name("RepairRecords")
nrows = worksheet.nrows
ncols = worksheet.ncols
print("行数：", nrows, "列数：", ncols)
for i in range(nrows):
    if i != 0:
        InputInfo = worksheet.row_values(i)
        print(InputInfo)
        bike = Bike.objects.get(BikeId=int(InputInfo[0]))
        center = Center.objects.get(CenterId=InputInfo[1])
        bdt = InputInfo[2]
        bdt = datetime.strptime(bdt, "%Y-%m-%d")
        rt = InputInfo[3]
        rt = datetime.strptime(rt, "%Y-%m-%d")
        RP = RepairRecords(
            BikeId=bike,
            CenterId=center,
            BreakDownTime=bdt,
            RepairTime=rt,
            RepairParts=InputInfo[4],
            Brake=InputInfo[5],
            Wheel=InputInfo[6],
            Pedal=InputInfo[7],
            Saddle=InputInfo[8],
            QRcode=InputInfo[9],
            Lock=InputInfo[10],
            Chain=InputInfo[11]
        )
        if RP.save_if_valid():
            print("Yes!")
        else:
            print(RP._errors)


# 插入第五张表

worksheet = workbook.sheet_by_name("CompanyInfo")
nrows = worksheet.nrows
ncols = worksheet.ncols
print("行数：", nrows, "列数：", ncols)
for i in range(nrows):
    if i != 0:
        InputInfo = worksheet.row_values(i)
        print(InputInfo)
        CI = CompanyInfo(
            CompanyName=InputInfo[0],
            BikeNumAll=InputInfo[1],
            BikeNumRun=InputInfo[2],
            BikeNumRepair=InputInfo[3]
        )
        if CI.save_if_valid():
            print("Yes!")
        else:
            print(CI._errors)


# 插入第六张表

worksheet = workbook.sheet_by_name("IllegalParking")
nrows = worksheet.nrows
ncols = worksheet.ncols
print("行数：", nrows, "列数：", ncols)
for i in range(nrows):
    if i != 0:
        InputInfo = worksheet.row_values(i)
        print(InputInfo)
        bike = Bike.objects.get(BikeId=int(InputInfo[0]))
        pt = datetime.strptime(InputInfo[4], "%Y-%m-%d %H:%M:%S")
        IP = IllegalParking(
            BikeId=bike,
            UserId=InputInfo[1],
            LocationX=InputInfo[2],
            LocationY=InputInfo[3],
            ParkingTime=pt
        )
        if IP.save_if_valid():
            print("Yes!")
        else:
            print(IP._errors)

