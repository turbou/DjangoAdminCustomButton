# Generated by Django 2.0.13 on 2019-12-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosukoi', '0003_oyoyo_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='oyoyo',
            name='filepath',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ファイルパス'),
        ),
    ]
