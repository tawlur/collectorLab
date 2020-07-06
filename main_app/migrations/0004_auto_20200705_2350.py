# Generated by Django 3.0.7 on 2020-07-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200705_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('skill', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(to='main_app.Driver'),
        ),
    ]
