# Generated by Django 3.2.8 on 2021-11-24 14:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0002_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('git', models.URLField()),
                ('startDate', models.DateField()),
                ('finishDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('authorEmail', models.EmailField(max_length=254)),
                ('text', models.CharField(max_length=250)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiteApp.blogs')),
            ],
        ),
    ]
