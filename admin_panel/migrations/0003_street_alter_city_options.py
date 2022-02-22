# Generated by Django 4.0.2 on 2022-02-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_city_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'street',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'managed': False, 'verbose_name_plural': 'cities'},
        ),
    ]