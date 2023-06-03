# Generated by Django 4.2.1 on 2023-06-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_alter_board_created_date_alter_board_updated_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='starred',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='workspace',
            name='website',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
