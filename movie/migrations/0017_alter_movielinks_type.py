# Generated by Django 4.0.4 on 2022-06-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_alter_movielinks_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielinks',
            name='type',
            field=models.CharField(choices=[('W', 'WATCH LINK'), ('D', 'DOWNLOAD LINK')], max_length=1),
        ),
    ]
