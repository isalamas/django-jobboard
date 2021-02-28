# Generated by Django 3.1.7 on 2021-02-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='title',
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
