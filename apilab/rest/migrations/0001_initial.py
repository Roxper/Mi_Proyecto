# Generated by Django 4.0.5 on 2022-06-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('update', models.DateTimeField()),
            ],
        ),
    ]