# Generated by Django 3.1.3 on 2021-01-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_sendemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendemail',
            name='subject',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]