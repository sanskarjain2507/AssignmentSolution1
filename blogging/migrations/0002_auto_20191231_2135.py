# Generated by Django 3.0.1 on 2019-12-31 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='charDuptBlog',
            new_name='charblog_updated_content',
        ),
        migrations.AddField(
            model_name='blogs',
            name='fileblog_content',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='fileblog_updated_content',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
