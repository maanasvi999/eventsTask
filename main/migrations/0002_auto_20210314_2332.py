# Generated by Django 3.1.4 on 2021-03-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventdetails',
            options={'verbose_name_plural': 'Events Details'},
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='image',
            field=models.ImageField(upload_to='main/images/'),
        ),
    ]