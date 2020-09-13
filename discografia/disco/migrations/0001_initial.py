# Generated by Django 3.0.5 on 2020-07-07 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albuns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título album')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albuns',
                'ordering': ['-titulo'],
            },
        ),
        migrations.CreateModel(
            name='Bandas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Banda')),
            ],
            options={
                'verbose_name': 'Banda',
                'verbose_name_plural': 'Bandas',
                'ordering': ['-nome'],
            },
        ),
        migrations.CreateModel(
            name='Musicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Música')),
                ('segundos', models.IntegerField(default=0, verbose_name='Tempo')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disco.Albuns', verbose_name='Album')),
            ],
            options={
                'verbose_name': 'Musica',
                'verbose_name_plural': 'Musicas',
                'ordering': ['-titulo'],
            },
        ),
        migrations.AddField(
            model_name='albuns',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disco.Bandas', verbose_name='Banda'),
        ),
    ]
