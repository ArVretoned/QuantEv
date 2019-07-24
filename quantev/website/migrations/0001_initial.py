# Generated by Django 2.2.3 on 2019-07-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('inventory_level', models.IntegerField()),
            ],
        ),
    ]