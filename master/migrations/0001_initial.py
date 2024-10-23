# Generated by Django 5.1.1 on 2024-10-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategori_produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True)),
                ('kode', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='pelanggan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=12)),
                ('nama', models.CharField(max_length=100)),
                ('tgl_lahir', models.DateField(blank=True)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pembayaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=5, null=True)),
            ],
        ),
    ]
