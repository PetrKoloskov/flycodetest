# Generated by Django 3.0.8 on 2020-07-27 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creationpost', '0002_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(height_field=100, null=True, upload_to='images', width_field=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]