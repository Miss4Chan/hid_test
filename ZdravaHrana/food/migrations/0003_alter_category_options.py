# Generated by Django 4.2 on 2023-06-03 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_productsinsale'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
