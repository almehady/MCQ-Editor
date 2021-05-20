# Generated by Django 3.2.2 on 2021-05-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210514_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionbank',
            name='add_model_test',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='other_exam',
            field=models.CharField(blank=True, help_text='write the exam name here', max_length=500, null=True),
        ),
    ]