# Generated by Django 2.1.7 on 2019-03-02 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20190302_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='hello.Post'),
        ),
    ]
