# Generated by Django 3.0.5 on 2020-12-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsroom', '0002_auto_20201213_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='poests',
            name='description',
        ),
    ]
