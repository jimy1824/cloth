from django.db import models
from colorfield.fields import ColorField


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)
        abstract = True


class CategoryComponents(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Component Name")
    key = models.CharField(max_length=250, unique=True, help_text="Component Key")

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}-{self.key}"


class Category(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Product Category Name")
    key = models.CharField(max_length=250, unique=True, help_text="Product Category Key")
    components = models.ManyToManyField(CategoryComponents, blank=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}-{self.key}"


class Body(TimeStampedModel):
    FRONT = 'front'
    BACK = 'back'
    SIDE_CHOICES = [
        (FRONT, 'Front'),
        (BACK, 'Back'),
    ]
    name = models.CharField(max_length=250, help_text="Sleeve Name")
    body_side = models.CharField(max_length=24, choices=SIDE_CHOICES)
    top_view = models.ImageField(upload_to='uploads/body/top')
    middle_view = models.ImageField(upload_to='uploads/body/middle')
    bottom_view = models.ImageField(upload_to='uploads/body/bottom')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Sleeve(TimeStampedModel):
    RIGHT = 'left'
    LEFT = 'right'
    SIDE_CHOICES = [
        (RIGHT, 'Right'),
        (LEFT, 'Left'),
    ]
    name = models.CharField(max_length=250, help_text="Sleeve Name")
    open_view = models.CharField(max_length=24, choices=SIDE_CHOICES)
    top_view = models.ImageField(upload_to='uploads/salves/top')
    right_view = models.ImageField(upload_to='uploads/salves/left')
    left_view = models.ImageField(upload_to='uploads/salves/right')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Collar(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Collar Name")
    design_image = models.ImageField(upload_to='uploads/collar/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Hood(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Hood Name")
    design_image = models.ImageField(upload_to='uploads/Hood/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Cuff(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Cuff Name")
    design_image = models.ImageField(upload_to='uploads/Cuff/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Pocket(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Pocket Name")
    design_image = models.ImageField(upload_to='uploads/Pocket/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class SleevePocket(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Sleeve Pocket Name")
    design_image = models.ImageField(upload_to='uploads/Pocket/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class PantsPocket(TimeStampedModel):
    FRONT = 'front'
    BACK = 'back'
    SIDE_CHOICES = [
        (FRONT, 'Front'),
        (BACK, 'Back'),
    ]
    name = models.CharField(max_length=250, help_text="Sleeve Pocket Name")
    body_side = models.CharField(max_length=24, choices=SIDE_CHOICES)
    design_image = models.ImageField(upload_to='uploads/Pocket/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Zip(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Pocket Name")
    design_image = models.ImageField(upload_to='uploads/Zip/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Strap(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Strap Name")
    design_image = models.ImageField(upload_to='uploads/Strap/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class StrapBuckle(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Strap Buckle Name")
    design_image = models.ImageField(upload_to='uploads/Buckle/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Rope(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Rope Name")
    design_image = models.ImageField(upload_to='uploads/Rope/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Hem(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Hem Name")
    design_image = models.ImageField(upload_to='uploads/Hem/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Lining(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Lining Name")
    design_image = models.ImageField(upload_to='uploads/Hem/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Bottom(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Bottom Name")
    design_image = models.ImageField(upload_to='uploads/Bottom/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Pants(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Bottom Name")
    design_image = models.ImageField(upload_to='uploads/Bottom/')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class FabricCategory(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Fabric Category Name")

    def __str__(self):
        return f"{self.name}"


class Color(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Color Name")
    color_code = ColorField(default='#FF0000')

    def __str__(self):
        return f"{self.name}"


class Fabric(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Fabric Name")
    short_description = models.CharField(max_length=250, help_text="Short Description", blank=True, null=True)
    category = models.ForeignKey(FabricCategory, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color)

    def __str__(self):
        return f"{self.category.name}--{self.name}"


class SizeFieldModel(TimeStampedModel):
    height = models.FloatField()
    width = models.FloatField()

    def __str__(self):
        return f"height={self.height}--width={self.height}"


class ProductSizeModel(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Product Component Name")
    size = models.ForeignKey(SizeFieldModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}--{self.size}"


class ProductDesign(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Product Category Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    front_view = models.ImageField(upload_to='uploads/', blank=True, null=True)
    back_view = models.ImageField(upload_to='uploads/', blank=True, null=True)
    body = models.ManyToManyField(Body, blank=True)
    sleeves = models.ManyToManyField(Sleeve, blank=True)
    collars = models.ManyToManyField(Collar, blank=True)
    hoods = models.ManyToManyField(Hood, blank=True)
    cuffs = models.ManyToManyField(Cuff, blank=True)
    pockets = models.ManyToManyField(Pocket, blank=True)
    pants_pocket = models.ManyToManyField(PantsPocket, blank=True)
    sleeve_pocket = models.ManyToManyField(SleevePocket, blank=True)
    zip = models.ManyToManyField(Zip, blank=True)
    straps = models.ManyToManyField(Strap, blank=True)
    straps_buckle = models.ManyToManyField(StrapBuckle, blank=True)
    ropes = models.ManyToManyField(Rope, blank=True)
    hems = models.ManyToManyField(Hem, blank=True)
    Linings = models.ManyToManyField(Lining, blank=True)
    pents = models.ManyToManyField(Pants, blank=True)
    bottoms = models.ManyToManyField(Bottom, blank=True)
    fabric = models.ManyToManyField(Fabric)
    sizes = models.ManyToManyField(ProductSizeModel)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"
