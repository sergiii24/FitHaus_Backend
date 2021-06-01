# Generated by Django 3.1.7 on 2021-06-01 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('achivements', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.BooleanField(default=False)),
                ('achievement', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='achivements.achievement')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
