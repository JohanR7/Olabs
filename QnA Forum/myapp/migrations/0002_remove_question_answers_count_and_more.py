# Generated by Django 5.1.6 on 2025-02-25 06:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='description',
        ),
        migrations.RemoveField(
            model_name='question',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='upvotes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='views',
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='QuestionVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.CharField(choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')], max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='question_votes', through='myapp.QuestionVote', to=settings.AUTH_USER_MODEL),
        ),
    ]
