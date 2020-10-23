# Generated by Django 3.0.1 on 2020-10-21 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.CharField(max_length=64, unique=True)),
                ('content', models.TextField()),
                ('link', models.CharField(max_length=250, unique=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('author_photo', models.CharField(max_length=150)),
                ('author_screen_name', models.CharField(max_length=64)),
                ('author_name', models.CharField(max_length=64)),
                ('author_describtion', models.CharField(max_length=250)),
                ('title', models.CharField(default='title', max_length=250)),
                ('thumnail_photo', models.CharField(default='<img class="img rounded img-raised" src="threader.com:8000/static/assets/img/bg27.jpg"> height="300" width="400"', max_length=150)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='post_dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('username', models.ManyToManyField(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]