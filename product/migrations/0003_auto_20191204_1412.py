# Generated by Django 2.2.7 on 2019-12-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191125_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='timestamp',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='username',
            new_name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
