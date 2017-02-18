from django.db import models
PAYMENT_OPTIONS = (
    ('MC', 'Mastercard'),
    ('VS', 'Visa'),
    ('PP', 'Paypal'),
    ('DT', 'Debit'),
)

#-------- testing section --------
class User(models.Model):
    username = models.CharField(max_length=75,)
    company = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20,)
    description = models.CharField(max_length=450, null=True)
    password = models.CharField(max_length=25,)
    subscriptionStatus = models.BooleanField(default=False)
    memberStatus = models.BooleanField(default=False)
    def __str__(self):
        return self.username

#-------- Payment Section --------   
class Payment(models.Model):
    

    method = models.CharField(max_length=2, choices=PAYMENT_OPTIONS)
    ccardHolder = models.CharField(max_length=50)
    ccardNumber1 = models.CharField(max_length=4)
    ccardNumber2 = models.CharField(max_length=4)
    ccardNumber3 = models.CharField(max_length=4)
    ccardNumber4 = models.CharField(max_length=4)
    ccardExpDateMth = models.CharField(max_length=2)
    ccardExpDateYr = models.CharField(max_length=2)
    ccardSecurity = models.CharField(max_length=3)
            
    def __str__(self):
        return self.method       

#-------- Property section --------
class PropertyType(models.Model):
    typeCode = models.CharField(max_length=20)
    typeName = models.CharField(max_length=255)

    def __str__(self):
        return self.typeName

    def as_json(self):
        return {'value':self.id,'text':self.typeName}

# Create table in sqlite + data.
#class UnitOfMeasure(models.Model):
#    UOMCode = models.CharField(max_length=5)
#    UOMValue = models.Number(max_length=15)
#
#    def __str__(self):
#        return self.typeName
#
#    def as_json(self):
#        return {'value':self.id,'text':self.typeName}

class BuildingType(models.Model):
    buildingCode = models.CharField(max_length=20)
    buildingName = models.CharField(max_length=255)

    def __str__(self):
        return self.buildingName

    def as_json(self):
        return {'value':self.id,'text':self.buildingName}

class Property(models.Model):
        
    projectNum = models.CharField(max_length=45)
    client = models.CharField(max_length=45)
    
    # break this down to address, province, city, postal code
    address = models.CharField(max_length=255)
    propertyTypeId = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, blank = True, null = True)
    #TODO (not in db)
    #buildingTypeId = models.ForeignKey(BuildingType, on_delete=models.SET_NULL, blank = True, null = True)

    # should have measure unit
    propertySize = models.DecimalField(max_digits=10, decimal_places=2)

    # TODO: create table & form.
    # unitOfMeasure = models.ForeignKey(UnitOfMeasure, on_delete=models.SET_NULL, blank = True, null = True)
    
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

