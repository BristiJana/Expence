# Generated by Django 3.2.9 on 2021-11-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('User_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=225)),
                ('Password', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bankac_id', models.IntegerField()),
                ('Bank_name', models.CharField(max_length=225)),
                ('Total_balance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('cat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.IntegerField()),
                ('cat_id', models.IntegerField()),
                ('Name', models.CharField(max_length=225)),
                ('Amount', models.FloatField()),
                ('Date', models.DateTimeField()),
                ('Details', models.CharField(max_length=225)),
                ('Bankac_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.IntegerField()),
                ('Income', models.FloatField()),
                ('Otherpay', models.FloatField()),
                ('Date', models.IntegerField()),
                ('Bankac_id', models.IntegerField()),
                ('Total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=225)),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=225)),
                ('dob', models.DateTimeField()),
                ('Budget', models.FloatField()),
            ],
        ),
    ]
