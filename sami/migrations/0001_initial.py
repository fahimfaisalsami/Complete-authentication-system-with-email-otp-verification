# Generated by Django 5.0.1 on 2024-01-23 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=7)),
            ],
        ),
    ]
