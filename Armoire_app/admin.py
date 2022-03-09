from django.contrib import admin

from .models import User, Piece, Outfit, PieceToOutfit
# Register your models here.
admin.site.register(User)
admin.site.register(Piece)
admin.site.register(Outfit)
admin.site.register(PieceToOutfit)
