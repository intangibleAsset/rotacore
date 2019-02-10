# Generated by Django 2.1 on 2019-02-10 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(blank=True, max_length=10, null=True)),
                ('firstName', models.CharField(blank=True, max_length=10, null=True)),
                ('lastName', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='shift date')),
                ('startTime', models.DateTimeField(verbose_name='shift start')),
                ('endTime', models.DateTimeField(verbose_name='shift end')),
                ('notes', models.TextField(blank=True, null=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Employee')),
            ],
        ),
    ]
