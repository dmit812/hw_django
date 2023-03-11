# Generated by Django 3.1.2 on 2023-03-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=None)),
                ('image', models.URLField(default=None)),
                ('release_date', models.DateField(default=None)),
                ('lte_exists', models.BooleanField(default=None)),
                ('slug', models.SlugField(default=None)),
            ],
        ),
    ]
