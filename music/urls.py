from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    	# ex: /polls/5/
	path('index.html', views.index, name='index'),
	path('piece/composer_index.html', views.pieces_by_composer, name='pieces_by_composer'),
	path('piece/index.html', views.piece_index, name='pieces_index'),
	path('box/index.html', views.box_list, name='box_list'),
	path('piece/index_csv.html', views.index_csv, name='piece_index_csv'),
	path('box/<int:box_id>/index_csv.html', views.box_csv, name='box_csv'),
	path('box/index_csv.html', views.boxlist_csv, name='boxlist_csv'),
	path('box/<int:box_id>/', views.box_detail, name='box_detail'),
	path('piece/<int:piece_id>/', views.piece_detail, name='piece_detail'),
]

