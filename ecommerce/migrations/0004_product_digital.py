# Generated by Django 3.1.1 on 2020-09-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
