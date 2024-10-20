# Generated by Django 5.1.2 on 2024-10-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0003_alter_pet_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_publication', models.DateField(auto_now_add=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, to='pets.pet')),
            ],
        ),
    ]
