from django.db import models


# Create your models here.



class Employee(models.Model):
    empname = models.CharField(max_length=200)
    emppassword = models.CharField(max_length=200)
    emporder = models.IntegerField(choices=((0, '无权限'),
                                            (1, '普通员工：查看权限，上架下架'),
                                            (2, '仓库管理员：增删改'),), default=0)
    empposit = models.CharField(max_length=200)
    empphone = models.CharField(max_length=200)




    class Meta():
        db_table = 'Employee'
    """
    def str(self):
       name = '1'
       password = '1'
       str1 = Emploee.objects.filter(empname=name, emppassword=password)

       if str1:
           order = str1.emporder

   """


class Depot(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # manager = models.IntegerField() #仓库管理员的ID
    manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta():
        db_table = 'Depot'


class Present(models.Model):
    name = models.CharField(max_length=200)
    on_date = models.DateTimeField()
    store_num = models.IntegerField()
    status = models.IntegerField(default=0) #0代表审核， 1代表上架， 2代表上架
    cost = models.DecimalField(max_digits=11, decimal_places=2)
    hot = models.IntegerField(default=0)
    off = models.IntegerField(default=0) #0代表不打折， 1代表打折
    off_cost = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    url = models.CharField(max_length=200, null=True)
    #pdepot = models.ManyToManyField(Depot, through='depot_present')

    class Meta():
        db_table = 'Present'


class depot_present(models.Model):
    depot = models.ForeignKey(Depot)
    present = models.ForeignKey(Present)

    add_reason = models.CharField(max_length=200, null=True)

    class Meta():
        db_table = 'depot_present'

