from django.db import models


# Create your models here.



class Employee(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    order = models.IntegerField(choices=((0, '无权限'),
                                            (1, '普通员工：查看权限，上架下架'),
                                            (2, '仓库管理员：增删改'),), default=0)
    posit = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

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


class Item(models.Model):
    name = models.CharField(max_length=200)
    store_num = models.IntegerField()
    location = models.CharField(max_length=200)
    purchase_date = models.DateTimeField()
    status = models.IntegerField(default=0) #0代表审核， 1代表上架， 2代表上架
    purchase_price = models.DecimalField(max_digits=11, decimal_places=2)
    depot = models.ForeignKey(
        Depot,
        on_delete=models.CASCADE
    )

    class Meta():
        db_table = 'Item'


class Category(models.Model):
    name = models.CharField(max_length=200)
    hot = models.IntegerField(null=True)

    class Meta():
        db_table = 'Category'


class Present(models.Model):
    name = models.CharField(max_length=200)
    introduction = models.CharField(max_length=200, null=True)
    on_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=11, decimal_places=2)
    hot = models.IntegerField(default=0)
    off = models.IntegerField(default=0) #0代表不打折， 1代表打折
    off_cost = models.DecimalField(max_digits=3, decimal_places=2, default=0, null=True)
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta():
        db_table = 'Present'


class CarouselMap(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    start_day = models.DateField()
    end_day = models.DateField()
    priority = models.IntegerField()
    present = models.ForeignKey(
        Present,
        on_delete=models.CASCADE
    )

    class Meta():
        db_table = 'CarouselMap'

#
# class User(models.Model):
#     name = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     birthday = models.DateTimeField()
#     nickname = models.CharField(max_length=200)
#     gender = models.IntegerField()
#     phone = models.CharField(max_length=200)
#
#
# class Comment(models.Model):
#     content = models.CharField(max_length=200)
#     comment_date = models.DateTimeField()
#     level = models.IntegerField()
#     user_id = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )
#     present_id = models.ForeignKey(
#         Present,
#         on_delete=models.CASCADE
#     )


