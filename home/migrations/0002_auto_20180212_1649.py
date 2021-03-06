# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 13:49
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hidden_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Часть текста, открывающаяся скриптом', verbose_name='Скрытый текст'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='open_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Открытая часть текста', verbose_name='Видимый текст'),
        ),
    ]
