# Generated by Django 3.1.8 on 2021-07-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='collection_name',
            field=models.CharField(max_length=100),
        ),
    ]
