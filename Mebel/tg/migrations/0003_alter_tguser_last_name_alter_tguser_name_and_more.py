# Generated by Django 4.1 on 2022-09-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0002_alter_tguser_lang_alter_tguser_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='last_name',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='name',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user_name',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
    ]