# Generated by Django 5.0.7 on 2024-07-23 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=40)),
                ('course_name', models.CharField(max_length=100)),
                ('course_credits', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_code', models.CharField(max_length=100)),
                ('meeting_dt', models.DateField(auto_now_add=True)),
                ('meeting_subject', models.CharField(max_length=100)),
                ('meeting_np', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=100)),
                ('student_sem', models.IntegerField()),
                ('enrolment', models.ManyToManyField(to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptopic', models.CharField(max_length=200)),
                ('plangauges', models.CharField(max_length=200)),
                ('pduration', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
