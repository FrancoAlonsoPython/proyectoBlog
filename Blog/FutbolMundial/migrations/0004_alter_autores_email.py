# Generated by Django 4.2.2 on 2023-07-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FutbolMundial', '0003_autores_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autores',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]
