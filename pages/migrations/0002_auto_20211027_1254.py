# Generated by Django 3.2.8 on 2021-10-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
