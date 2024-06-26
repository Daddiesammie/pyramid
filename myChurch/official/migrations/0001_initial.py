# Generated by Django 5.0.2 on 2024-02-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='official_photos')),
                ('description', models.TextField()),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
