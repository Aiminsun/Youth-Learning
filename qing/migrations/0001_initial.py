# Generated by Django 3.0.5 on 2020-11-06 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data_img', models.CharField(blank=True, max_length=255, null=True)),
                ('data_str', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Data',
                'managed': True,
            },
        ),
    ]
