# Generated by Django 5.1.1 on 2024-10-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts'),
        ),
    ]