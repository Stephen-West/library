from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=12)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class Box(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    @property
    def url(self):
        return "http://martleweb.co.uk/music/{b}/index.html".format(b=self.id)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class Composer(models.Model):
    surname = models.CharField(max_length=30)
    first_names = models.CharField(max_length=50, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True) 
    role = models.CharField(max_length=30, blank=True, null=True)
    dates =  models.CharField(max_length=30, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        string = self.surname
        if self.first_names:
            string+=", {n}".format(n=self.first_names)
        if self.suffix:
            string += ", {s}".format(s=self.suffix)
        if self.role:
            string += " ({r})".format(r=self.role)
        return string
    class Meta:
        ordering = ('surname','first_names','suffix')

class Piece(models.Model):
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    composed_by =  models.ManyToManyField(Composer)
    publisher =  models.ForeignKey(Publisher, on_delete=models.CASCADE)
    original_ref = models.CharField(max_length=30, blank=True, null=True)
    instrument = models.CharField(max_length=20)
    parts = models.PositiveIntegerField(default=1)
    box =  models.ForeignKey(Box, on_delete=models.CASCADE)
    number_of_copies = models.PositiveIntegerField(default=1)
    borrowed_from = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True) 
    def __str__(self):
        string = "{n} NO COMPOSER".format(n=self.name)
        if self.composed_by:
            composers = self.composed_by.all()
            composer_list = list(composers)
            if len(composer_list)>0:
                string = "{n} ({c})".format(n=self.name, c=composer_list[0])

        return string
    class Meta:
        ordering = ('name',)


