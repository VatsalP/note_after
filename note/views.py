import string
import random

from django.shortcuts import render


def gen_id(size=8, chars=string.ascii_letters + string.digits):
    """ Generates link_id
    """
    return "".join(
        random.SystemRandom().choice(chars) for _ in range(size)
    )


def index(request):
    return render(request, 'note/index.html')


def get_note(request, id):
    pass
