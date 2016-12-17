from django.db import models

class Inspector(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    # for login
    # username = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    # commentId = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # from former customer
    # ...

    #re-write it with format()
    def __str__(self):
        return self.firstname + ' ' + self.lastname  

class Owner(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname + ' ' + self.lastname  

#-------- Property section --------
class PropertyType(models.Model):
    typeCode = models.CharField(max_length=20)
    typeName = models.CharField(max_length=255)

    def __str__(self):
        return self.typeName  

class BuildingType(models.Model):
    buildingCode = models.CharField(max_length=20)
    buildingName = models.CharField(max_length=255)

    def __str__(self):
        return self.buildingName  

class Property(models.Model):
    ownerId = models.ForeignKey(Owner, on_delete=models.CASCADE, blank = True, null = True)
    # can set a different inspector
    inspectorId = models.ForeignKey(Inspector, on_delete=models.SET_NULL, blank = True, null = True)

    # break this down to address, province, city, postal code
    address = models.CharField(max_length=255)
    propertyTypeId = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, blank = True, null = True)

    # should have measure unit
    propertySize = models.DecimalField(max_digits=10, decimal_places=2)
    buildingTypeId = models.ForeignKey(BuildingType, on_delete=models.SET_NULL, blank = True, null = True)

    # should have createdById, take from logged user
    createdDate = models.DateTimeField(auto_now_add = True)

    #never delete from database, just hide it when query
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.address

#-------- Room section --------
class RoomType(models.Model):
    # even with random name, can use also
    roomCode = models.CharField(max_length=20)
    roomTypeName = models.CharField(max_length=255)

    def __str__(self):
        return self.roomTypeName  

class Room(models.Model):
    propertyId = models.ForeignKey(Property, on_delete=models.CASCADE)
    roomTypeId = models.ForeignKey(RoomType, on_delete=models.SET_NULL, blank = True, null = True)
    roomName = models.CharField(max_length=255)

    def __str__(self):
        return self.roomName  

#-------- Component section --------
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def validate_file_extension(value):
    extArray = ['.png', '.jpg']

    for ext in extArray:
        if not value.name.endswith(ext):
            raise ValidationError(u'Error file type')

class Component(models.Model):
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE)
    componentName = models.CharField(max_length=255)
    faultDescription = models.CharField(max_length=1000)
    # should be multiple photos
    # tutorial on codeschool
    # faultPhoto = models.ImageField(upload_to='uploads', validators=[validate_file_extension], default = 'static/inspection/images/beautiful-girl.jpg')
    def __str__(self):
        return self.componentName  

