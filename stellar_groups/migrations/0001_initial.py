# Generated by Django 4.2.16 on 2024-11-13 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StellarGroup',
            fields=[
                ('id', models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('description_html', models.TextField(blank=True, default='', editable=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StellarGroupMember',
            fields=[
                ('id', models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='stellar_groups.stellargroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stellar_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('group', 'user')},
            },
        ),
        migrations.AddField(
            model_name='stellargroup',
            name='members',
            field=models.ManyToManyField(through='stellar_groups.StellarGroupMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
