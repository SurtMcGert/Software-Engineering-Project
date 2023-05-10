# Generated by Django 4.1.7 on 2023-04-24 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DiscussionApp', '0003_chatmessage_chatroom_discussionboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='parentMessage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DiscussionApp.chatmessage'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
