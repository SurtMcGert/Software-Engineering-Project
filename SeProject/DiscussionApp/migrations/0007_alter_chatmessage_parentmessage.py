# Generated by Django 4.1.7 on 2023-04-25 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DiscussionApp', '0006_merge_20230425_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='parentMessage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DiscussionApp.chatmessage'),
        ),
    ]
