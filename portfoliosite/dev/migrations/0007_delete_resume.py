# Generated by Django 4.0.3 on 2022-08-06 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0006_alter_resume_maps_alter_resume_perm'),
    ]

    operations = [
        migrations.DeleteModel(
            name='resume',
        ),
    ]