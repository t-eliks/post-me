# Generated by Django 2.1.7 on 2019-03-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_auto_20190302_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='publish_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Published on'),
        ),
    ]
