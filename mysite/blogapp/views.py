from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post
import datetime



def index(request):
    kk = ''
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       test_type = request.POST['test_type']
       content = request.POST['content']
       post = Post(title=title)
       post.last_update = datetime.datetime.now() 
       post.test_type = test_type
       post.content = content
       
       post.save()
       kk = "123"
    # Get all posts from DB
    posts = Post.objects 
    return render_to_response('index.html', {'abc': kk},
                              context_instance=RequestContext(request))


def update(request):
    id = eval("request." + request.method + "['id']")
    post = Post.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']

        post.last_update = datetime.datetime.now() 
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': Post.objects} 

    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['id']")

    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete() 
        template = 'mysubmit.html'
        params = {'Posts': Post.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))

def mysubmit(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       test_type = request.POST['test_type']
       content = request.POST['content']
       post = Post(title=title)
       post.last_update = datetime.datetime.now() 
       post.test_type = test_type
       post.content = content
       
       post.save()

    # Get all posts from DB
    posts = Post.objects 
    return render_to_response('mysubmit.html', {'Posts': posts},
                              context_instance=RequestContext(request))


import uuid


  #read cache user id
def read_from_cache():
    key = datetime
    reg_id = cache.get(key)
    return reg_id

#write cache user id
def write_to_cache(data):
    key = datetime
    cache.set(key, data, 60*1)

def get_id():
  return  str(uuid.uuid4())[:11].replace('-', '').lower() 

@cache_page(30)
def register(request):
    reg_id = get_id
    write_to_cache(reg_id)
    #return  render_to_response('register.html', {'reg_id': 1234})
    return render_to_response('register.html', {'reg_id': reg_id},
                              context_instance=RequestContext(request))

