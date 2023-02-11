# Generated by Django 4.1.3 on 2023-01-07 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('ish_vaqti', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('sahifa', models.SmallIntegerField()),
                ('janr', models.CharField(choices=[('Badiiy', 'Badiiy'), ('Ilmiy', 'Ilmiy'), ('Hujjatli', 'Hujjatli')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('tugilgan_yil', models.DateField()),
                ('tirik', models.BooleanField()),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('kitob_soni', models.PositiveSmallIntegerField(default=0)),
                ('kurs', models.PositiveSmallIntegerField()),
                ('bitiruvchi', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateField()),
                ('qaytardi', models.BooleanField(default=False)),
                ('qaytargan_sana', models.DateField(blank=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.admin')),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.kitob')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.talaba')),
            ],
        ),
        migrations.AddField(
            model_name='kitob',
            name='muallif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.muallif'),
        ),
    ]
