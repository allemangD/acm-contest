# Generated by Django 2.2.6 on 2019-10-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_auto_20191012_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='solution',
            field=models.TextField(blank=True, null=True),
        ),
    ]