# Generated by Django 3.2.6 on 2021-09-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='senhaCriptografada',
            new_name='sala',
        ),
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(default='email@example.com', max_length=60),
            preserve_default=False,
        ),
    ]
