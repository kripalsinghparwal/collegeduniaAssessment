# Generated by Django 4.0.4 on 2022-04-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('total_runs', models.IntegerField()),
                ('out', models.IntegerField()),
                ('balls', models.IntegerField()),
                ('average', models.DecimalField(decimal_places=6, max_digits=10)),
                ('strikerate', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
    ]