# Generated by Django 3.2.2 on 2021-06-08 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ModelTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='P', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='questionbank',
            name='media',
        ),
        migrations.RemoveField(
            model_name='questionbank',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='questionbank',
            name='add_model_test',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='questionbank',
            name='explanation_image',
            field=models.ImageField(blank=True, null=True, upload_to='explanation/'),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='c1',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='c2',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='c3',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='exam_year',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='issue',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='o_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='other_exam',
            field=models.CharField(blank=True, help_text='write the exam list here', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='subject',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
        migrations.AddField(
            model_name='questionbank',
            name='model_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.modeltest'),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
    ]
