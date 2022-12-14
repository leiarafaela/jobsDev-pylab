# Generated by Django 4.1.3 on 2022-11-13 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_alter_vagas_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='tecnologias_dominadas',
            field=models.ManyToManyField(null=True, to='empresa.tecnologias'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='tecnologias_estudar',
            field=models.ManyToManyField(null=True, related_name='estudar', to='empresa.tecnologias'),
        ),
    ]
