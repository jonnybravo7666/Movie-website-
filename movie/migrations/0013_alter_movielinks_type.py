# Generated by Django 4.0.4 on 2022-06-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_movielinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielinks',
            name='type',
            field=models.CharField(choices=[('W', 'WATCH LINK'), ('D', 'DOWNLOAD LINK')], max_length=1),
        ),
    ]
