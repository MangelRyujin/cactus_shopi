# Generated by Django 4.2.2 on 2023-06-11 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cactus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoy_name',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='plants_image/', verbose_name='Imagen del producto'),
        ),
    ]