# Generated by Django 4.2 on 2023-04-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_password_user_age_user_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password1',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='introduction',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='password2',
            field=models.CharField(max_length=20),
        ),
    ]
