# Generated by Django 3.0.3 on 2020-02-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20200204_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='exception_text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
