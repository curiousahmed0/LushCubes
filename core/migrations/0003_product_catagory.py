# Generated by Django 4.2.1 on 2023-06-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_carousal'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(blank=True, choices=[('M', 'Men'), ('W', 'Women'), ('K', 'Kids')], max_length=3, null=True),
        ),
    ]
