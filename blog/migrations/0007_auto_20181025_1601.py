# Generated by Django 2.1.2 on 2018-10-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_blog_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_url',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
