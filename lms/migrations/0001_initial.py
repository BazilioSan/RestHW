# Generated by Django 5.1.4 on 2024-12-21 08:41

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
                ('title', models.CharField(help_text='Введите название курса', max_length=255, unique=True, verbose_name='Название курса')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='lms/previews', verbose_name='Превью')),
                ('description', models.TextField(blank=True, help_text='Введите описание курса', null=True, verbose_name='Описание курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название урока', max_length=255, verbose_name='Название урока')),
                ('description', models.CharField(help_text='Введите описание урока', max_length=255, verbose_name='Описание урока')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='lms/previews', verbose_name='Превью')),
                ('video', models.URLField(max_length=255)),
                ('course', models.ForeignKey(help_text='Выберите курс', on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]