# Generated by Django 3.2.12 on 2022-09-05 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_book_issue_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 22, 18, 18, 203882)),
        ),
    ]
