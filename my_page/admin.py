from django.contrib import admin

from .models import Protein,Animal


#这里设置的是django后台管理界面，显示数据的项目
@admin.register(Protein)
class ProteinAdmin(admin.ModelAdmin):
	list_display = ('id','pro_name')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
	list_display = ('id','name','family_name','category_name','species_name','kind')
