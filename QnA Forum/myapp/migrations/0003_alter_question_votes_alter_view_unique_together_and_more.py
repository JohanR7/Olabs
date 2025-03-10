# Generated by Django 5.1.6 on 2025-02-26 03:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_question_answers_count_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='question_votes', through='myapp.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='view',
            unique_together={('question', 'session_id', 'ip_address')},
        ),
        migrations.DeleteModel(
            name='QuestionVote',
        ),
    ]
