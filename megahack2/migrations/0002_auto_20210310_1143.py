# Generated by Django 3.1.7 on 2021-03-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megahack2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='website_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
