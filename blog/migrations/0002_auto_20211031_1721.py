# Generated by Django 3.2.8 on 2021-10-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='Human Rights', max_length=200),
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.CharField(default='Human Rights', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='words',
            field=models.IntegerField(default=400),
        ),
    ]