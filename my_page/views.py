from django.shortcuts import render_to_response,get_object_or_404
from .models import Animal,Protein
# Create your views here.

#这个函数是用于显示主页的
def page_index(request):
	return render_to_response('page_index.html')

#这个是用于显示一个列表，显示所有物种基本信息的列表
def page_ani_list(request,mark):
	content = {}
	if int(mark) == 1:
		content['kind']='鱼'
		content['animals'] = Animal.objects.filter(kind='鱼')
	if int(mark) == 2:
		content['kind']='虾'
		content['animals'] = Animal.objects.filter(kind='虾')
	if int(mark) == 3:
		content['kind']='蟹'
		content['animals'] = Animal.objects.filter(kind='蟹')
	if int(mark) == 4:
		content['kind']='甲壳'
		content['animals'] = Animal.objects.filter(kind='甲壳')
	return render_to_response('page_ani_list.html',content)

#用于显示过敏原的基本信息
def page_pro_list(request):
	content = {}
	content['protein'] = Protein.objects.all()
	return render_to_response('page_pro_list.html',content)
#显示每个过敏原的光谱图
def page_pro_pic(request,index):
	content = {}
	content['animal'] = Animal.objects.filter(id=int(index[:-1]))
	content['pic_name'] = index
	print(content['animal'])
	return render_to_response('page_pro_pic.html',content)
#显示红外光谱的基本介绍
def page_spe(request):
	return render_to_response('page_spe.html')
#返回实验室的基本信息
def page_lab(request):
	return render_to_response('page_lab.html')