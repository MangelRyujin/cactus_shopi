from django.db import models

# Create your models here.

class Category(models.Model):
    
    category_name = models.CharField('Nombre de la categoria', max_length=255, blank=False , null=False, unique=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.categoy_name


class Plant(models.Model):
    """Model definition for Pnatas."""
    name = models.CharField('Nombre de la planta', max_length=255, blank=False , null=False)
    description = models.TextField('Descripcion', blank= False, null=False)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    image = models.ImageField('Imagen del producto', upload_to='plants_image/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Plant."""

        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

    def __str__(self):
        return self.name
