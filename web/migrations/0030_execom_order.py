# Generated by Django 2.0.4 on 2019-06-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_merge_20190620_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='execom',
            name='order',
            field=models.IntegerField(null=True, verbose_name='Order'),
        ),
    ]