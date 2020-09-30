from django.shortcuts import render,HttpResponse,redirect
from home.models import Books
# Create your views here.
from .forms import BookForm
def home(request):
    allbooks=Books.objects.all()
    context={
        'allbooks':allbooks
    }
    return render(request,'index.html',context)



def additems(request):

    if request.method=='POST':
        title=request.POST['title']
        author=request.POST['author']
        publisher=request.POST['publisher']
        stock=request.POST['stock']
        item_obj=Books(title=title,author=author,publisher=publisher,stock=stock)
        item_obj.save()
    return redirect("/")  


def delete_data(request,sno):
    allbooks=Books.objects.all()
    context={
        'allbooks':allbooks
    }
    if request.method=='POST':
        pi= Books.objects.get(pk=sno)   
        pi.delete()
        return redirect("/")



def update_data(request,sno):
    if request.method== 'POST':
        pi= Books.objects.get(pk=sno)
        fm=BookForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= Books.objects.get(pk=sno)
        fm=BookForm(instance=pi)       
    return render(request,'update.html',{'form':fm})

def highstock(request):
    pi= Books.objects.all().order_by('stock')
    context={
        'pi':pi
    }
    return render(request,'highstock.html',context)


def lowstock(request):
    pi= Books.objects.all().order_by('-stock')
    context={
        'pi':pi
    }
    return render(request,'lowstock.html',context) 

def publisher(request):
    pi= Books.objects.all().order_by('publisher')
    context={
        'pi':pi
    }
    return render(request,'publisher.html',context) 


def search(request):
    query=request.GET['query']
    allPosts=Books.objects.filter(title__icontains=query)
    params={'allPosts':allPosts}
    return render(request,'search.html',params)       
