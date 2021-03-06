# Generated by Django 3.2.7 on 2021-10-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptLifeApp', '0003_adoption_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('testimonial_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('photo', models.URLField()),
            ],
        ),
    ]
