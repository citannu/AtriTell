# Generated by Django 4.0.5 on 2022-07-05 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AtriTell', '0002_user_tg_user_id_alter_user_tg_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_user_id',
            field=models.BigIntegerField(null=True, unique=True),
        ),
        migrations.CreateModel(
            name='TgChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(unique=True)),
                ('tg_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='tg_user_id')),
            ],
        ),
    ]
