# -*- coding: utf-8 -*-
# czat/czat/admin.py

from django.contrib import admin
from czat.models import Wiadomosc # importujemy nasz model

# rejestrujemy model Wiadomosc w panelu administracyjnym
admin.site.register(Wiadomosc)
