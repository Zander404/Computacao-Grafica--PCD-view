# Generated by Django 4.2.7 on 2023-11-30 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcd_render', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='discomfort',
            new_name='Desconforto',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='nausea',
            new_name='Desconforto Estomacal',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='describe',
            new_name='Descrição',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='stomach',
            new_name='Nausea',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='name',
            new_name='Nome Completo',
        ),
    ]
