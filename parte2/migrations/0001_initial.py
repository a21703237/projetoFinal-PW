# Generated by Django 3.2.3 on 2021-07-04 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('apelido', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=9)),
                ('ano_nascimento', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=120)),
                ('question2', models.CharField(max_length=120)),
                ('question3', models.CharField(max_length=120)),
                ('question4', models.CharField(max_length=120)),
                ('question5', models.CharField(max_length=120)),
                ('question6', models.CharField(max_length=120)),
                ('question7', models.CharField(max_length=120)),
                ('question8', models.CharField(max_length=120)),
                ('question9', models.CharField(max_length=120)),
                ('question10', models.CharField(max_length=120)),
            ],
        ),
    ]