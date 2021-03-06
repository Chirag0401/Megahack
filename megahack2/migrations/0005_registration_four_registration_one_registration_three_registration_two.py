# Generated by Django 3.1.7 on 2021-03-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megahack2', '0004_code_of_conduct_rule_view_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration_four',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='registration_one',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='registration_three',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='registration_two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
