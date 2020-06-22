from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def list_view(req):
	note = Note.objects.all()
	context = {
		'note': note
	}
	return render(req, 'list.html', context)

def insert_view(req):
	noteForm = NoteForm(req.POST or None)
	if req.method == 'POST':
		if noteForm.is_valid():
			noteForm.save()
		return redirect("dashboard:list")
	context = {
		'noteForm' : noteForm
	}
	return render(req, 'insert.html', context)

def delete_view(req, delete_id):
	Note.objects.filter(id = delete_id).delete()
	return redirect("dashboard:list")

def update_view(req, update_id):
	noteForm_lama = Note.objects.get(id = update_id)
	data = {
		'judul': noteForm_lama.judul,
		'isi': noteForm_lama.isi,
	}
	noteForm = NoteForm(req.POST or None, initial = data, instance = noteForm_lama)
	if req.method == 'POST':
		if noteForm.is_valid():
			noteForm.save()
		return redirect("dashboard:list")
	context = {
		'noteForm': noteForm
	}
	return render(req, 'insert.html', context)