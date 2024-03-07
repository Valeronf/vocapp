# Generated by Django 5.0.1 on 2024-01-31 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_alter_word_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.theme'),
        ),
    ]