from django.shortcuts import render, redirect
from star.models import Posts
from taggit.models import Tag
from .forms import PostsForm
from django.contrib.auth.decorators import login_required


def home(request):
    posts=Posts.objects.filter(status="да")

    context={'posts':posts}
    return render(request,'star/base.html',context)

@login_required
def new_post(request):
    #posts = Tag.objects.all()
    if request.method!="POST":
        form=PostsForm()
    else:
        form=PostsForm(data=request.POST)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.author = request.user
            new_post=form.save()
            return redirect('star:home')
    context={'form':form,}
    return render(request,'star/index.html',context)




def check_valve_data():
        data = {'size': [], 'publish':[]}

        valves = Posts.objects.all()

        for unit in valves:

            data['size'].append(unit.size)
            data['publish'].append(unit.publish)

        #print(data)
        return data

def graf(request):
        data = check_valve_data()
        print(data)
        d=[]
        for k in data.values():
            d.append(k)
            print(d)


        title = {"text": 'Check Valve Data'}
        series = [
            { "data": data['publish'],"значение": data['size']},
            ]


        return render(request, 'star/graf.html', {'data': data,
                                              'title': title,
                                                'series': series})


