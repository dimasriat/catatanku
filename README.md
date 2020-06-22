# django-dynamic-page

1. EDIT settings.py

    ```python
    INSTALLED_APPS = [
    	# ...
    	'crud',
    ]

    TEMPLATES = [
    	{
    		# ...
    		'DIRS': ['templates'],
    		# ...
    	},
    ]

    DATABASES = {
    	'default': {
    		'ENGINE': 'django.db.backends.mysql',
    		'NAME': 'djangonote',
    		'USER':'root',
    		'PASSWORD':'',
    		'HOST': 'localhost',
    		'PORT': '3306',
    	}
    }

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
    	os.path.join(BASE_DIR, 'static')
    ]

    ```

1. BUAT models.py (app)

    ```python
    from django.db import models

    class Produk(models.Model):
    	nama = models.CharField(max_length = 100)
    	deskripsi = models.CharField(max_length = 100)
    	harga = models.CharField(max_length = 100)
    	def __str__(self):
    		return "{}".format(self.id)
    ```

1. BUAT forms.py (app)

    ```python
    from django import forms
    from .models import Produk

    class ProdukForm(forms.ModelForm):
    	class Meta:
    		model = Produk
    		fields = ['nama', 'deskripsi', 'harga']
    ```

1. BUAT admin.py (app)

    ```python
    from django.contrib import admin
    from .models import Produk

    admin.site.register(Produk)
    ```

1. BUAT urls.py (app)

    ```python
    from django.conf.urls import url
    from . import views

    app_name = 'crud'
    urlpatterns = [
    	url(r'^$', views.list_view, name="list"),
    	url(r'^insert/$', views.insert_view, name="insert"),
    	url(r'^update/(?P<update_id>[0-9]+)$', views.update_view, name="update"),
    	url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete_view, name="delete"),
    ]
    ```

1. BUAT views.py (app)

    ```python
    from django.shortcuts import render, redirect
    from .models import Produk
    from .forms import ProdukForm

    def list_view(req):
    	produk = Produk.objects.all()
    	context = {
    		'produk': produk
    	}
    	return render(req, 'list.html', context)

    def insert_view(req):
    	produkForm = ProdukForm(req.POST or None)
    	if req.method == 'POST':
    		if produkForm.is_valid():
    			produkForm.save()
    		return redirect("crud:list")
    	context = {
    		'produkForm' : produkForm
    	}
    	return render(req, 'insert.html', context)

    def delete_view(req, delete_id):
    	Produk.objects.filter(id = delete_id).delete()
    	return redirect("crud:list")

    def update_view(req, update_id):
    	produkForm_lama = Produk.objects.get(id = update_id)
    	data = {
    		'nama' : produkForm_lama.nama,
    		'deskripsi': produkForm_lama.deskripsi,
    		'harga' : produkForm_lama.harga,
    	}
    	produkForm = ProdukForm(req.POST or None, initial = data, instance = produkForm_lama)
    	if req.method == 'POST':
    		if produkForm.is_valid():
    			produkForm.save()
    		return redirect("crud:list")
    	context = {
    		'produkForm' : produkForm
    	}
    	return render(req, 'insert.html', context)
    ```

1. BUAT list.html (app)
    ```html
    <h1>list page</h1>
    <table>
    	<tr>
    		<th>no</th>
    		<th>nama</th>
    		<th>deskripsi</th>
    		<th>harga</th>
    		<th>aksi</th>
    	</tr>
    	{% for barang in produk %}
    	<tr>
    		<td>{{ forloop.counter }}</td>
    		<td>{{ barang.nama }}</td>
    		<td>{{ barang.deskripsi }}</td>
    		<td>{{ barang.harga }}</td>
    		<td>
    			<a href="{% url 'crud:update' barang.id %}">update</a>
    			<a href="{% url 'crud:delete' barang.id %}">hapus</a>
    		</td>
    	</tr>
    	{% endfor %}
    </table>
    ```
1. BUAT insert.html (app)
    ```html
    <h1>insert / update page</h1>
    <form method="POST">
    	{% csrf_token %}
    	<table>
    		{{ produkForm.as_table }}
    	</table>
    	<button type="submit">KIRIM</button>
    </form>
    ```
