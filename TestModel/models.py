from django.db import models
import django.utils.timezone as timezone
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

#共享单车
class Bike(models.Model):
    StateChoices = (
        (1,'可用'),
        (0,'待维修'),
    )
    BikeId = models.CharField(primary_key=True,max_length=6,verbose_name='平台统一编号') #主键
    CompanyName = models.CharField(max_length=10,verbose_name='所属企业')
    BikeState = models.IntegerField(choices=StateChoices,default='可用')
    LocationX = models.DecimalField(max_digits=6,decimal_places=3,verbose_name='经度')
    LocationY = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='纬度')
    LaunchTime = models.DateField(editable=True,default=timezone.now,verbose_name='投放时间')
    Battery = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],verbose_name='电量')
    ServiceLife = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(3)],verbose_name='使用年限')

    class Meta:
        db_table = "Bike"
        verbose_name = 'Bike'


#骑行记录
class CyclingRecords(models.Model):
    BikeId = models.ForeignKey(Bike,on_delete=models.CASCADE) #外键
    UserId = models.CharField(max_length=11,verbose_name='骑行用户id')
    StartTime = models.DateTimeField(editable=True,default=timezone.now,verbose_name='开始时间')
    EndTime = models.DateTimeField(editable=True,default=timezone.now,verbose_name='结束时间')
    LocationX = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='经度')
    LocationY = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='纬度')

    class Meta:
        db_table = "CyclingRecords"
        verbose_name = 'CyclingRecords'


#维修记录
class RepairRecords(models.Model):
    StateChoices = (
        (1,'损坏'),
        (0,'完好'),
    )

    BikeId = models.ForeignKey(Bike,on_delete=models.CASCADE) #外键
    BreakDownTime = models.DateField(editable=True,default=timezone.now,verbose_name='损坏发生时间')
    RepairTime = models.DateField(editable=True,default=timezone.now,verbose_name='维修完成时间')
    CenterId = models.CharField(max_length=3,verbose_name='维修中心编号')
    RepairParts = models.CharField(max_length=7,verbose_name='维修部位')
    Brake = models.IntegerField(choices=StateChoices,verbose_name='刹车')
    Wheel = models.IntegerField(choices=StateChoices,verbose_name='车轮')
    Pedal = models.IntegerField(choices=StateChoices,verbose_name='脚踏')
    Saddle = models.IntegerField(choices=StateChoices,verbose_name='车座')
    QRcode = models.IntegerField(choices=StateChoices,verbose_name='二维码')
    Lock = models.IntegerField(choices=StateChoices,verbose_name='车锁')
    Chain = models.IntegerField(choices=StateChoices,verbose_name='链条')
    Remark = models.CharField(max_length=200,verbose_name='备注')

    class Meta:
        db_table = "RepairRecords"
        verbose_name = 'RepairRecords'

#维修中心
class Center(models.Model):
    CenterId = models.CharField(primary_key=True,max_length=3,verbose_name='维修中心编号')
    Location = models.CharField(max_length=20,verbose_name='地址')
    BrakeNum = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(0)],verbose_name='刹车数量')
    WheelNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='车轮数量')
    PedalNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='脚踏数量')
    SaddleNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='车座数量')
    QRcodeNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='二维码数量')
    LockNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='车锁数量')
    ChainNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='链条数量')

    class Meta:
        db_table = "Center"
        verbose_name = 'Center'

# 共享单车企业类CompanyInfo
class CompanyInfo(models.Model):
    CompanyName = models.CharField(primary_key=True, max_length=10, verbose_name="企业名称")
    BikeNumAll = models.IntegerField(validators=[MaxValueValidator(999999),
                                                 MinValueValidator(0)],
                                     verbose_name="共享单车总数")
    BikeNumRun = models.IntegerField(validators=[MaxValueValidator(999999),
                                                 MinValueValidator(0)],
                                     verbose_name="运营单车总数")
    BikeNumRepair = models.IntegerField(validators=[MaxValueValidator(999999),
                                                    MinValueValidator(0)],
                                        verbose_name="维修单车总数")
    CompanyIncome = models.IntegerField(null=False, verbose_name="运营收入")

    class Meta:
        db_table = "CompanyInfo"
        verbose_name = 'CompanyInfo'


# 违停情况类 IllegalParking
class IllegalParking(models.Model):
    BikeId = models.ForeignKey(Bike, on_delete=models.CASCADE)  # 外键
    UserId = models.CharField(max_length=11, verbose_name='骑行用户id')
    LocationX = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='经度')
    LocationY = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='纬度')
    ParkingTime = models.DateField(editable=True,auto_now=True, verbose_name='停车时间')

    class Meta:
        db_table = "IllegalParking"
        verbose_name = 'IllegalParking'


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=30,unique=True,)
#     password = models.CharField(max_length=30,)
#     permission = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(1)],verbose_name='权限')
#     create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
#     is_delete = models.BooleanField(default=False,verbose_name="删除")
#
#     class Meta:
#         ordering = ['create_time','id']
#         db_table = "User"