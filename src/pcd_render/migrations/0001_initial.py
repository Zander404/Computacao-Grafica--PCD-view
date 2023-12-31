# Generated by Django 4.2.7 on 2023-11-30 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('nausea', models.CharField(choices=[('F', 'Forte'), ('M', 'Moderada'), ('L', 'Leve'), ('N', 'Nenhuma')], max_length=1)),
                ('stomach', models.CharField(choices=[('F', 'Forte'), ('M', 'Moderada'), ('L', 'Leve'), ('N', 'Nenhuma')], max_length=1)),
                ('discomfort', models.CharField(choices=[('F', 'Forte'), ('M', 'Moderada'), ('L', 'Leve'), ('N', 'Nenhuma')], max_length=1)),
                ('describe', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
