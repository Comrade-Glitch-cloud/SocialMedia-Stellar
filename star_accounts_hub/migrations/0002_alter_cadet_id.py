# Generated by Django 4.2.16 on 2024-11-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star_accounts_hub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
