# Generated by Django 2.2.5 on 2019-09-25 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('mesa', models.IntegerField()),
                ('atividade', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='ItemComanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Choice')),
                ('comanda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Comanda')),
            ],
        ),
    ]
