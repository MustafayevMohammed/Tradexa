# Generated by Django 3.2.6 on 2021-10-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.IntegerField(verbose_name='Price:'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='weight',
            field=models.IntegerField(verbose_name='Weight:'),
        ),
    ]
