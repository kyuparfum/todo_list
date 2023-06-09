# Generated by Django 4.2 on 2023-04-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default=1, max_length=3, verbose_name='age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.TextField(default=1, verbose_name='introduction'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password1',
            field=models.CharField(default=1, max_length=20, verbose_name='password1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=1, max_length=20, verbose_name='password2'),
            preserve_default=False,
        ),
    ]
