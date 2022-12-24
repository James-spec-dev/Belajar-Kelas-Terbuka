# Generated by Django 4.1.4 on 2022-12-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('jurnal', 'jurnal'), ('olahraga', 'olahraga'), ('ekonomi', 'ekonomi')], default='jurnal', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='PostModel',
        ),
    ]
