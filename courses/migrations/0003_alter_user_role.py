# Generated by Django 5.1.2 on 2024-10-20 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('instructor', 'Instructor'), ('student', 'Student')], max_length=20),
        ),
    ]