# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Music 
from django.contrib.auth.decorators import login_required


@login_required
def all_music(request):
    musics = music.objects.all()
    return render(request, "music/music.html",
                  {"music": music})

