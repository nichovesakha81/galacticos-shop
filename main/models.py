from django.db import models
from django.contrib.auth.models import User

# Pembuatan model pada aplikasi main dengan nama Product
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('merchandise', 'Merchandise'),
        ('accessories', 'Accessories'),
    ]

    # Atribut-atribut yang wajib ada dalam models.py
    name = models.CharField(max_length=255)  # Nama produk
    price = models.IntegerField()  # Harga produk
    description = models.TextField()  # Deskripsi produk
    thumbnail = models.URLField()  # URL gambar produk
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Kategori
    is_featured = models.BooleanField(default=False)  # Status unggulan

    # Atribut tambahan yang saya tambahkan & ini opsional
    stock = models.PositiveIntegerField(default=0)  # Stok barang
    brand = models.CharField(max_length=100, blank=True, null=True)  # Merk produk
    rating = models.FloatField(default=0.0)  # Rating produk
    
    # Agar representasi str dari object Product ditampilkan dengan nama + harga (lebih mudah dibaca)
    def __str__(self):
        return f"{self.name} - Rp{self.price:,}"