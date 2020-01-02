from django.shortcuts import render,redirect
from .models import Blogs
from django.core.files.storage import FileSystemStorage
from collections import OrderedDict
from django.utils import timezone
from problem1.settings import BASE_DIR

#This method define homepage
def index(request):
   blogs=Blogs.objects.order_by('-createdTime')
   d=OrderedDict()
   for i in blogs:
       if i.fileblog:
           content=i.fileblog_updated_content.split('\n')
           d[i.id]=[content,'fileblog']
       elif i.charblog:
           d[i.id]=[i.charblog_updated_content,'charblog']
   return render(request,'blogging/index.html',{'blogs':d})

#This method will go to page that will input charblog
def onCharPress(request):
    return render(request, 'blogging/charinput.html')

#This method will go to page that will input fileblog
def onFilePress(request):
    return render(request, 'blogging/fileinput.html')

#This is method is called after file is input and submit button is clicked
def after_fileInput(request):
    if request.method=='POST':
                file1=request.FILES['filed']
                fs = FileSystemStorage()
                filename = fs.save(file1.name, file1)
                file_url=fs.url(filename)
                fp = open(BASE_DIR + str(file_url), 'r',encoding='utf8')

                content=fp.read()
                form=Blogs(fileblog=file_url,fileblog_content=content,fileblog_updated_content=content)
                form.save()
                return redirect('/blogging')

#This is method is called after characters are input and submit button is clicked
def after_charInput(request):
    if request.method == 'POST':
        chars = request.POST.get('chars')
        form = Blogs(charblog=chars,charblog_updated_content=chars)
        form.save()
        return redirect('/blogging')

#This method is called after update button is clicked
def after_updt(request):
    id=request.GET.get('blg_updt')
    print(id)
    data=Blogs.objects.filter(id=id)
    if data[0].fileblog:
        content = data[0].fileblog_updated_content
        return render(request,'blogging/updt_file.html',{'blog':content,'id':id})
    else:
        content=data[0].charblog_updated_content
        return render(request, 'blogging/updt_char.html', {'blog': content,'id':id})

#This method defines functionality to update charblog
def after_charInput_updt(request):
    id = request.POST.get('id')
    data = Blogs.objects.filter(id=id)
    old_content = data[0].charblog_updated_content
    new_content = request.POST.get('chars')
    if old_content!=new_content:
        Blogs.objects.filter(id=id).update(charblog=old_content, charblog_updated_content=new_content,updationTime=timezone.now())
    return redirect('/blogging')

#This method defines functionality to update fileblog
def after_fileInput_updt(request):
    id=request.POST.get('id')
    data=Blogs.objects.filter(id=id)
    old_content=data[0].fileblog_updated_content
    new_content=request.POST.get('files')
    n=new_content.split('\n')
    if old_content!=new_content:
        fp = open(BASE_DIR + str(data[0].fileblog), 'w',encoding='utf8')
        fp.writelines(n)
        fp.close()
        Blogs.objects.filter(id=id).update(fileblog_content=old_content,fileblog_updated_content=new_content,updationTime=timezone.now())

    return redirect('/blogging')

#This method will show all the updates
def show_updt(request):
    data=Blogs.objects.order_by("-updationTime")
    print(data)
    d = OrderedDict()
    for i in data:
        if i.fileblog:
            content = i.fileblog_content
            updt_content=i.fileblog_updated_content
            if i.updationTime==i.createdTime:
                action_is='creation'
            else:
                action_is='updation'
            d[i.id] = [content, 'File Blog',updt_content,action_is]
        elif i.charblog:
            content = i.charblog
            updt_content = i.charblog_updated_content
            if i.updationTime==i.createdTime:
                action_is='creation'
            else:
                action_is='updation'
            d[i.id] = [content, 'Char Blog',updt_content,action_is]
    return render(request,'blogging/updated_contents.html',{'blogs':d})