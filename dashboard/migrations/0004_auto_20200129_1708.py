# Generated by Django 3.0.2 on 2020-01-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200129_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
