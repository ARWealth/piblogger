# Generated by Django 4.2.1 on 2023-05-12 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pibloggers', '0002_blogpost_title_delete_pibloggerpost_blogpost_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'blog_posts'},
        ),
    ]
