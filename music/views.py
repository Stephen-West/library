from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Piece, Box, Publisher,Composer

def queryset_to_csv(qs, response):
    """
    Takes in a Django queryset and spits out a CSV file.
	
    Usage::
	
		>> from dummy_app.models import *
		>> qs = DummyModel.objects.all()
		>> queryset_to_csv(qs, './data/dump.csv')
	
	Based on a snippet by zbyte64::
		
		http://www.djangosnippets.org/snippets/790/
	
	"""
    model = qs.model
    headers = []
    for field in model._meta.fields:
        headers.append(field.name)
    writer = csv.writer(response)
    writer.writerow(headers)
	
    for obj in qs:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            #if type(val) == unicode:
             #   val = val.encode("utf-8")
            row.append(val)
        writer.writerow(row)
    return response

def index(request):
    number_of_pieces = Piece.objects.count()
    number_of_boxes = Box.objects.count()
    number_of_composers = Composer.objects.count()
    context = {
        'number_of_pieces'    : number_of_pieces,
        'number_of_boxes'     : number_of_boxes,
        'number_of_composers' : number_of_composers,
        }
    return render(request, 'music/frontpage.html', context)

def piece_index(request):
    piece_list = Piece.objects.order_by('name')
    #template = loader.get_template('music/index.html')
    for p in piece_list:
        print (p.id, p.name)
    context = {'piece_list': piece_list }
    return render(request, 'music/index.html', context)

class composer_structure:
    def __init__(self):
        self.composer_name = ""
        self.piece_list=0
    
def old_pieces_by_composer(request):
    composers = Composer.objects.order_by('surname')
    piece_list = Piece.objects.order_by('name')
    full_list=[]
    for c in composers:
        pieces_for_this_composer =[]
        for p in piece_list:
            if c in p.composed_by.all():
                pieces_for_this_composer.append(p)
                #print ("Adding {p} to {n}".format(p=p.name, n=name))
        s = composer_structure()
        s.composer_name = str(c)
        s.piece_list = pieces_for_this_composer
        full_list.append(s)
        
    context = {'piece_list': full_list }
    return render(request, 'music/composer_index.html', context)

def pieces_by_composer(request):
    composers = Composer.objects.order_by('surname')
    full_list=[]
    for c in composers:
        pieces= c.piece_set.all()
        s = composer_structure()
        s.composer_name = str(c)
        s.piece_list = pieces
        full_list.append(s)
        
    context = {'piece_list': full_list }
    return render(request, 'music/composer_index.html', context)

def box_list(request):
    box_list = Box.objects.order_by('name')
    #template = loader.get_template('music/index.html')
    context = {'box_list': box_list }
    return render(request, 'music/box_list.html', context)

def box_detail(request, box_id):
    this_box = Box.objects.get(id=box_id)
    box_contents = Piece.objects.filter(box_id=box_id).order_by('name')
    context = { 'pieces' : box_contents,
                'this_box' : this_box }
    return render (request, 'music/box_contents.html', context)

def piece_detail(request, piece_id):
    this_piece = Piece.objects.get(id=piece_id)
    context = { 'piece' : this_piece,}
    return render (request, 'music/piece_detail.html', context)

import csv
from django.http import HttpResponse

def index_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="music_index.csv"'
    piece_list = Piece.objects.order_by('name')
    #writer = csv.writer(response)
    #writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    queryset_to_csv(piece_list, response)
    return response

def box_csv(request, box_id):
    this_box = Box.objects.get(id=box_id)
    box_contents = Piece.objects.filter(box_id=box_id)
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    csv_filename="box_{b}.csv".format(b=str(box_id))
    disposition = 'attachment; filename={f}'.format(f=csv_filename)
    response['Content-Disposition'] = disposition
    queryset_to_csv(box_contents, response)
    return response

def boxlist_csv(request):
    box_list = Box.objects.order_by('name')
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    csv_filename="box_list.csv"
    disposition = 'attachment; filename={f}'.format(f=csv_filename)
    response['Content-Disposition'] = disposition
    queryset_to_csv(box_list, response)
    return response
