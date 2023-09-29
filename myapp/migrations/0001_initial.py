# Generated by Django 4.2.5 on 2023-09-29 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('is_avaliable', models.BooleanField(default=False)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
