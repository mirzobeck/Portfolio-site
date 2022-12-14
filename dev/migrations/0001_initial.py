# Generated by Django 4.0.3 on 2022-08-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=30)),
                ('year_of_birth', models.DateField()),
                ('year_of_programming', models.DateField()),
                ('work', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('fullabout', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='works/')),
                ('workurl', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
