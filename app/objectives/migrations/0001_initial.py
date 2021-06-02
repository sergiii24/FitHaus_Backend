# Generated by Django 3.1.7 on 2021-06-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('objective', models.CharField(choices=[('S', 'Salut'), ('Fr', 'Força'), ('P', 'Perdua'), ('Fl', 'Flexibilitat'), ('Rs', 'Resistencia'), ('Rc', 'Recuperacio'), ('A', 'Agilitat')], max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
