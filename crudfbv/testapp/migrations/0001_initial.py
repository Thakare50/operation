# Generated by Django 3.2.19 on 2024-02-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('sage', models.IntegerField()),
                ('slocation', models.CharField(max_length=30)),
            ],
        ),
    ]
