# Generated by Django 3.2.8 on 2021-10-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
