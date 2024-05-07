from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=100)

class department_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    d_name=models.CharField(max_length=100)
    Details=models.TextField()

class volunteers_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    photo = models.FileField()
    aadharno= models.BigIntegerField()
    status = models.CharField(max_length=100)

class user_table(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)

class product_table(models.Model):
    productname = models.CharField(max_length=100)
    Description = models.TextField()
    image = models.FileField()
    stock = models.IntegerField()
    price = models.FloatField()

class need_table(models.Model):
    department= models.ForeignKey(department_table, on_delete=models.CASCADE)
    needs= models.CharField(max_length=100)
    details= models.CharField(max_length=300)
    amount= models.FloatField()
    date=models.DateField()
    status=models.CharField(max_length=100)


class needresponse(models.Model):
    userid = models.ForeignKey(user_table, on_delete=models.CASCADE)
    needid = models.ForeignKey(need_table, on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)
    amount = models.FloatField()


class foodchart_table(models.Model):
     day=models.CharField(max_length=100)
     daytime=models.CharField(max_length=100)
     daytype=models.CharField(max_length=100)
     amount = models.FloatField()

class fooddonation(models.Model):
    foodchart = models.ForeignKey(foodchart_table, on_delete=models.CASCADE)
    userid = models.ForeignKey(user_table, on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)
    amount = models.FloatField()


class inventory_table(models.Model):
     department = models.ForeignKey(department_table, on_delete=models.CASCADE)
     inventory = models.CharField(max_length=100)
     description = models.CharField(max_length=300)
     stock = models.IntegerField()

class inventoryrequest_table(models.Model):
    inventory= models.ForeignKey(inventory_table, on_delete=models.CASCADE)
    userid = models.ForeignKey(user_table, on_delete=models.CASCADE)
    date=models.DateField()
    stock = models.IntegerField()
    reason=models.CharField(max_length=100)
    status=models.CharField(max_length=100)



class  order_table(models.Model):
    userid = models.ForeignKey(user_table, on_delete=models.CASCADE)
    date=models.DateField()
    amount = models.FloatField()
    status=models.CharField(max_length=100)


class  orderdetail_table(models.Model):
    order = models.ForeignKey(order_table, on_delete=models.CASCADE)
    product = models.ForeignKey(product_table, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()







class  patientinfo_table(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob= models.DateField()
    sdate= models.DateField()
    phone = models.BigIntegerField()
    disease = models.CharField(max_length=100)
    Image = models.FileField()
    idproof = models.FileField()
    status = models.FileField()
    volunteer = models.ForeignKey(volunteers_table, on_delete=models.CASCADE)





class patient_enable(models.Model):
    patient_id =  models.ForeignKey(patientinfo_table, on_delete=models.CASCADE)
    reson =  models.CharField(max_length=100)
    status = models.FileField()
















