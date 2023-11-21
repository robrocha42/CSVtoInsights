# Generated by Django 4.2.7 on 2023-11-11 01:48

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='name',
            field=models.CharField(default='Funcionarios', max_length=128, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.FileField(storage=home.models.OverwriteStorage(), upload_to='home/'),
        ),
    ]