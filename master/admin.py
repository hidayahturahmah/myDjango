from django.contrib import admin

from pelanggan.models import pelanggan
from penjual.models import penjual
from produk.models import produk
from kategori_produk.models import kategori_produk
from pesanan.models import pesanan
from detail_pesanan.models import detail_pesanan
from pembayaran.models import pembayaran
from pengiriman.models import pengiriman
from review_produk.models import review_produk
from keranjang_belanja.models import keranjang_belanja


# Register your models here.
class PenjualAdmin(admin.ModelAdmin):
    list_display = ["id_seller", "nama_toko", "alamat", "no_telepon"]
admin.site.register(penjual, PenjualAdmin)

class AdminPelanggan(admin.ModelAdmin):
    list_display = ["nama", "email", "alamat"]
admin.site.register(pelanggan, AdminPelanggan)

class AdminProduk(admin.ModelAdmin):
    list_display = ["nama", "kode", "deskripsi"]
admin.site.register(produk, AdminProduk)

class AdminKategori_produk(admin.ModelAdmin):
    list_display = ["kode"]
admin.site.register(kategori_produk, AdminKategori_produk)

class AdminPesanan(admin.ModelAdmin):
    list_display = ["total_harga", "tanggal_order"]
admin.site.register(pesanan, AdminPesanan)

class AdminDetail_pesanan(admin.ModelAdmin):
    list_display = ["id_produk", "harga_subtotal"]
admin.site.register(detail_pesanan, AdminDetail_pesanan)

class AdminPembayaran(admin.ModelAdmin):
    list_display = ["nama", "kode"]
admin.site.register(pembayaran, AdminPembayaran)

class AdminPengiriman(admin.ModelAdmin):
    list_display = ["nama", "kode"]
admin.site.register(pengiriman, AdminPengiriman)

class AdminReview_produk(admin.ModelAdmin):
    list_display = ["deskripsi"]
admin.site.register(review_produk, AdminReview_produk)

class AdminKeranjang_belanja(admin.ModelAdmin):
    list_display = ["id_produk", "harga_subtotal"]
admin.site.register(keranjang_belanja, AdminKeranjang_belanja)
