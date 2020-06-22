from django.shortcuts import render

def index(req):
	context = {
		'deskripsi': 'selamat datang Resia! semoga hari-harimu menyenangkan 💖'
	}
	return render(req, 'index.html', context)