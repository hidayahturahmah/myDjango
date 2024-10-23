from django.db import models

# Create your models here.
class penjual(models.Model):
    id_seller = models.CharField(max_length=5)
    nama_toko = models.CharField(max_length=20, null=True)
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=13)

class pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    alamat = models.TextField()

    def __str__(self) -> str:
        return f"{self.nama}"

class produk(models.Model):
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=5)
    deskripsi = models.CharField()

class kategori_produk(models.Model):
    kode = models.CharField(null=True, blank=True)

class pesanan(models.Model):
    total_harga = models.CharField(max_length=10)
    tanggal_order = models.DateField(blank=True, null=True)

class detail_pesanan(models.Model):
    id_produk = models.CharField(max_length=5)
    harga_subtotal = models.CharField(max_length=100)

class pembayaran(models.Model):
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=5, null=True)

class keranjang_belanja(models.Model):
    id_produk = models.CharField(max_length=5)
    harga_subtotal = models.CharField(max_length=100)

class pengiriman(models.Model):
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=5, null=True)

class review_produk(models.Model):
    deskripsi = models.CharField()


       