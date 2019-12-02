from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import django.utils.timezone as timezone

# Create your models here.


class Bike(models.Model):
    BikeId = models.CharField(primary_key=True, max_length=6, verbose_name='平台统一编号')      # 主键
    CompanyName = models.CharField(max_length=10, verbose_name='所属企业')
    BikeState = models.BooleanField(default=True, verbose_name='可用')
    LocationX = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='经度')
    LocationY = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='纬度')
    LaunchTime = models.DateField(null=True, blank=True, default=None, verbose_name='投放时间')
    Battery = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='电量')
    ServiceLife = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(3)], verbose_name='使用年限')

    class Meta:
        db_table = 'Bike'
        verbose_name = 'Bike'


# 骑行记录
class CyclingRecords(models.Model):
    BikeId = models.ForeignKey(Bike, on_delete=models.CASCADE)          # 外键
    UserId = models.CharField(max_length=11, verbose_name='骑行用户id')
    StartTime = models.DateTimeField(default=timezone.now, verbose_name='开始时间')
    EndTime = models.DateTimeField(default=timezone.now, verbose_name='结束时间')
    LocationX = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='经度')
    LocationY = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='纬度')

    class Meta:
        db_table = "CyclingRecords"
        verbose_name = 'CyclingRecords'


# 维修中心
class Center(models.Model):
    CenterId = models.CharField(primary_key=True, max_length=3, verbose_name='维修中心编号')
    LocationX = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='经度')
    LocationY = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='纬度')
    BrakeNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='刹车数量')
    WheelNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='车轮数量')
    PedalNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='脚踏数量')
    SaddleNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='车座数量')
    QRcodeNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='二维码数量')
    LockNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='车锁数量')
    ChainNum = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name='链条数量')

    class Meta:
        db_table = "Center"
        verbose_name = 'Center'


# 维修记录
class RepairRecords(models.Model):
    BikeId = models.ForeignKey(Bike, on_delete=models.CASCADE)       # 外键
    CenterId = models.ForeignKey(Center, on_delete=models.CASCADE, verbose_name='维修中心编号')
    BreakDownTime = models.DateField(default=timezone.now, verbose_name='损坏发生时间')
    RepairTime = models.DateField(default=timezone.now, verbose_name='维修完成时间')
    RepairParts = models.CharField(max_length=7, verbose_name='维修部位')
    Brake = models.BooleanField(default=True, verbose_name='刹车')        # True代表完好，False代表损坏
    Wheel = models.BooleanField(default=True, verbose_name='车轮')
    Pedal = models.BooleanField(default=True, verbose_name='脚踏')
    Saddle = models.BooleanField(default=True, verbose_name='车座')
    QRcode = models.BooleanField(default=True, verbose_name='二维码')
    Lock = models.BooleanField(default=True, verbose_name='车锁')
    Chain = models.BooleanField(default=True, verbose_name='链条')
    Remark = models.CharField(null=True, blank=True, max_length=200, verbose_name='备注')

    class Meta:
        db_table = "RepairRecords"
        verbose_name = 'RepairRecords'


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

    class Meta:
        db_table = "CompanyInfo"
        verbose_name = 'CompanyInfo'


# 违停情况类 IllegalParking
class IllegalParking(models.Model):
    BikeId = models.ForeignKey(Bike, on_delete=models.CASCADE)  # 外键
    UserId = models.CharField(max_length=11, verbose_name='骑行用户id')
    LocationX = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='经度')
    LocationY = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='纬度')
    ParkingTime = models.DateTimeField(default=timezone.now, verbose_name='停车时间')

    class Meta:
        db_table = "IllegalParking"
        verbose_name = 'IllegalParking'
