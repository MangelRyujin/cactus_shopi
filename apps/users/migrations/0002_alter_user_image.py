# Generated by Django 4.2.2 on 2023-06-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='perfil/', verbose_name='imagen de perfil'),
        ),
    ]