# Generated by Django 4.1.1 on 2023-03-29 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0014_remove_udonation_ngo_remove_udonation_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='udonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.CharField(max_length=150)),
                ('amount', models.IntegerField(max_length=50)),
                ('status', models.CharField(max_length=150, null=True)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngoapp.ngo_reg')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngoapp.project')),
                ('reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngoapp.user_reg')),
            ],
        ),
        migrations.CreateModel(
            name='assigneddonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=150)),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngoapp.udonation')),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngoapp.ngo_reg')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngoapp.project')),
            ],
        ),
    ]
