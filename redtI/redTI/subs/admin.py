from django.contrib import admin
from .models import Subrediti, Thread, Post, Subscription

class SubreditiAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'criador']#o header das colunas
    search_fields = ['title', 'slug']#cria algo pra pesquisar
    prepopulated_fields = {'slug': ('title',)}#faz uma ligação doq é escrito em title para slug.

admin.site.register(Subrediti, SubreditiAdmin)#lembra que se a gente não colocar o segundo parâmetro vira o admin normal.
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Subscription)