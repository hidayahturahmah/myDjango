# Generated by Django 5.1.1 on 2024-10-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='penjual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_seller', models.CharField(max_length=12)),
                ('nama_toko', models.CharField(max_length=5, null=True)),
                ('alamat', models.TextField()),
                ('no_telepon', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='pesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_harga', models.CharField(max_length=10)),
                ('tanggal_order', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=5)),
                ('deskripsi', models.CharField()),
            ],
        ),
        migrations.DeleteModel(
            name='master',
        ),
        migrations.RemoveField(
            model_name='kategori_produk',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='pelanggan',
            name='nim',
        ),
        migrations.RemoveField(
            model_name='pelanggan',
            name='tgl_lahir',
        ),
        migrations.AddField(
            model_name='pelanggan',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='kategori_produk',
            name='kode',
            field=models.CharField(blank=True, null=True),
        ),
    ]
