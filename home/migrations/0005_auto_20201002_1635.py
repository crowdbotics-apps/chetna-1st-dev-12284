# Generated by Django 2.2.16 on 2020-10-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201002_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='abdcd',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='hjjhjhkj',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='uriyriw',
        ),
        migrations.AddField(
            model_name='customtext',
            name='jhkhk',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
