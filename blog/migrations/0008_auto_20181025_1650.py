# Generated by Django 2.1.2 on 2018-10-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181025_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_url',
            new_name='url1',
        ),
        migrations.AddField(
            model_name='blog',
            name='content1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
