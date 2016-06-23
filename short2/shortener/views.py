from shortener import models
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse

def home(request):  
    short_url = None
    long_url = None
    if request.method == "POST":
      link_db = models.Tableurl()
      link_db.link = request.POST.get("url")
      link_db.save()
      short_url = request.build_absolute_uri(link_db.get_short_id())
      id_long = link_db.decode_id(link_db.get_short_id())
      table_object =  get_object_or_404(models.Tableurl, id=id_long)
      long_url = table_object.link
      link_db.shortlink = short_url
      link_db.save()
    return render_to_response('shortener/home.html', {"long_url":long_url}, RequestContext(request,{"short_url":short_url}))

def link(request, id):
    db_id = models.Tableurl.decode_id(id)
    link_db = get_object_or_404(models.Tableurl, id=db_id)
    return redirect(link_db.link)    
