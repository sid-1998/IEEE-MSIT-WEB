# Generated by Django 2.0.4 on 2019-06-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_execom_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execom',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
