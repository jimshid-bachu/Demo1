# Generated by Django 3.1.4 on 2020-12-22 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.category'),
            preserve_default=False,
        ),
    ]
