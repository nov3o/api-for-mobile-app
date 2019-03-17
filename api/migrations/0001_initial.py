# Generated by Django 2.1.7 on 2019-03-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafeteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CafeteriaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafeteria_id', models.PositiveIntegerField()),
                ('image', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('schedule_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=40)),
                ('weight', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cal', models.PositiveSmallIntegerField()),
                ('image', models.TextField(max_length=20)),
                ('category_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Macroelements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proteins', models.FloatField()),
                ('fat', models.FloatField()),
                ('carbohydrats', models.FloatField()),
                ('food_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('cafeteria_id', models.PositiveIntegerField()),
                ('week_day', models.PositiveSmallIntegerField()),
            ],
        ),
    ]