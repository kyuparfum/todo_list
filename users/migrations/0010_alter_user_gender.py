# Generated by Django 4.2 on 2023-04-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_user_followings_user_is_active_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('여', '여자'), ('남', '남자')], max_length=1),
        ),
    ]
