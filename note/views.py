import string
import random

from django.shortcuts import render, redirect
from django.http import Http404

from .models import Note


def gen_id(size=8, chars=string.ascii_letters + string.digits):
    """ Generates link_id
    """
    return "".join(
        random.SystemRandom().choice(chars) for _ in range(size)
    )


def index(request):
    if request.method == 'POST':
        note_id = gen_id()
        note_text = request.POST.get('note')
        note = Note(note_id=note_id)
        note.note = note_text
        note.save()
        return redirect('/{}'.format(note_id))

    return render(request, 'note/index.html')


def get_note(request, id):
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        raise Http404
    note_text = note.note
    return render(request, 'note/note.html', {'note': note_text})
