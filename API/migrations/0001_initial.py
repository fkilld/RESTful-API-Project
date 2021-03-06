# Generated by Django 3.1.2 on 2020-10-11 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharityRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('CharityName', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ItemID', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('ItemName', models.CharField(max_length=200)),
                ('Quantity', models.IntegerField()),
                ('Category', models.CharField(max_length=200)),
                ('Charity', models.CharField(default='None', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('UserName', models.CharField(max_length=200)),
                ('CharityName', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('ItemName', models.CharField(max_length=200)),
                ('Quantity', models.IntegerField()),
                ('UserName', models.EmailField(max_length=254)),
                ('ItemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.item')),
            ],
        ),
    ]
