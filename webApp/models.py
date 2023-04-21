from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    
class about_model(models.Model):
    video_file = models.FileField(upload_to='videos/',null= True)
    description = models.CharField(max_length=255,null=True,blank=True)

class course_details(models.Model):
    image = models.ImageField(null=True,blank = True,upload_to = 'img/courses')
    course_name = models.CharField(max_length=255, null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    fee = models.IntegerField(null=True,blank=True)
    duration = models.CharField(max_length=100,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)

class course_description_list(models.Model):
    list_item = models.CharField(max_length=100)
    course = models.ManyToManyField('course_details')

class instructors(models.Model):
    image = models.ImageField(null=True,blank = True,upload_to = 'img/instructors')
    name = models.CharField(max_length=255, null=True,blank=True)
    designation = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)

class testimonial(models.Model):
    image = models.ImageField(null=True,blank = True,upload_to = 'img/testimonial')
    name = models.CharField(max_length=255, null=True,blank=True)
    profession = models.CharField(max_length=255,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)

class contactus(models.Model):

    name = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.CharField(max_length=255,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)

class gallery(models.Model):
    image = models.ImageField(null=True,blank = True,upload_to = 'img/gallery')

class enquiry(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    course = models.CharField(max_length=100,null=True,blank=True)
    message = models.CharField(max_length=255,null=True,blank=True)