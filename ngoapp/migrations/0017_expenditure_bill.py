# Generated by Django 4.1.1 on 2023-03-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0016_expenditure'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='bill',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
