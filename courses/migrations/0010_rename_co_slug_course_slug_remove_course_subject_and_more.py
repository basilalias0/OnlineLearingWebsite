# Generated by Django 4.1.7 on 2023-03-28 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_rename_slug_course_co_slug_alter_course_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='co_slug',
            new_name='slug',
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
