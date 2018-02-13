# Generated by Django 2.0.2 on 2018-02-12 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site2016', '0008_auto_20180209_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('descricao', models.TextField(verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'projeto',
                'verbose_name_plural': 'projetos',
            },
        ),
    ]
