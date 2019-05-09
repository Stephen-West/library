from django.contrib import admin

# Register your models here.

from .models import Box, Publisher, Piece, Composer

admin.site.register(Box)

admin.site.register(Publisher)

admin.site.register(Composer)

#admin.site.register(Piece)

#class LibraryAdmin(admin.ModelAdmin):
 #   filter_horizontal = ('composed_by',)
    

class PieceAdmin(admin.ModelAdmin):
    #list_filter =('group',)
    model=Piece
    filter_horizontal = ('composed_by',)
    search_fields = ['name']
    

admin.site.register(Piece, PieceAdmin)
