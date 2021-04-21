# Generated by Django 3.1.7 on 2021-04-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('S', 'Strength'), ('C', 'Cardio'), ('Y', 'Yoga'), ('E', 'Stretching'), ('R', 'Rehabilitation'), ('P', 'Pilates')], default='S', max_length=30)),
            ],
        ),
    ]
