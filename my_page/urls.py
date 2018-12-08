from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	#http://localhost:8000/pro,进入蛋白详情页
	path('pro',views.page_pro_list,name='pro_list'),
	#http://localhost:8000/ani,进入样品详情页
	url(r'ani/(\d+)/$',views.page_ani_list,name='ani_list'),
	url(r'pic/(1[0-9][A,B]|[1-9][A,B]|2[0-8][A,B])/$',views.page_pro_pic,name='pro_pic'),
	url(r'spe',views.page_spe,name='page_spe')
]
