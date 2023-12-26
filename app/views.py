from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

#------TOPIC
def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.order_by('topic_name')
    QLTO=Topic.objects.order_by('-topic_name')
    
    d = {'topics':QLTO}
    return render(request,'display_topics.html',d)

# inserting data into topic 
def insert_topic(request):
    tn = input('Enter topic name: ')
    TNO = Topic.objects.get_or_create(topic_name=tn)[0]
    TNO.save()
    
    QLTO=Topic.objects.all()
    d = {'topics':QLTO}
    return render(request,'display_topics.html',d)

def delete_topic(request):
    
    Topic.objects.filter(topic_name='Football').delete()
    
    QLTO = Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)





#-------WEBPAGE
def display_webpage(request):
    QLWO = Webpage.objects.all()
    
    # QLWO = Webpage.objects.order_by('topic_name')
    # QLWO = Webpage.objects.order_by('name')
    # QLWO = Webpage.objects.order_by('-topic_name')
    # QLWO = Webpage.objects.order_by('-name')
    
    QLWO = Webpage.objects.all()[7:10:]
    
    # QLWO = Webpage.objects.order_by(Length('topic_name'))
    # QLWO = Webpage.objects.order_by(Length('name'))
    # QLWO = Webpage.objects.order_by(Length('topic_name').desc())
    # QLWO = Webpage.objects.order_by(Length('name').desc())
    
    
    # QLWO = Webpage.objects.filter(id__gt=1)
    # QLWO = Webpage.objects.filter(id__gte=1)
    # QLWO = Webpage.objects.filter(id__lt=4)
    # QLWO = Webpage.objects.filter(id__lte=4)
    # QLWO = Webpage.objects.filter(name__startswith='D')
    # QLWO = Webpage.objects.filter(url__endswith='in')
    
    # QLWO = Webpage.objects.all()
    # QLWO = Webpage.objects.filter(name__startswith='d', url__endswith='.com')        # here normal queryset (and op performed by comma(,))
    # QLWO = Webpage.objects.filter(Q(name__startswith='r') & Q(url__endswith='.in'))  # here Q means query object which converting querysets to query object for concatenate
    # QLWO = Webpage.objects.filter(Q(name__startswith='r') | Q(url__endswith='.com')) # for or op Q obj must 
    # QLWO = Webpage.objects.filter(Q(topic_name='Cricket') & Q(url__endswith='in'))
    QLWO = Webpage.objects.all()

    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


# inserting data into webpage
def insert_webpage(request):
    tn=input('Enter topic name: ')
    n=input('Enter name: ')
    u=input('Enter url: ')
    e=input('Enter email: ')
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


# updating data
def update_webpage(request):
    
    # update() method
    
    Webpage.objects.filter(topic_name='Hockey').update(name='Henry')            # one row satisfied no error    
    Webpage.objects.filter(topic_name='Cricket').update(url='http://bcci.in')   # two row satisfied no error
    
    Webpage.objects.filter(topic_name='Cricket').update(url='http://bcci.in')   # two row satisfied no error

    Webpage.objects.filter(name='Dhoni').update(email='dhoni@gamil.com')
    Webpage.objects.filter(name='Virat').update(email='virat@gamil.com')
    Webpage.objects.filter(name='Rohit').update(email='rohit@gamil.com')
    
    
    
    # update_or_create()
    
    # Webpage.objects.update_or_create(topic_name='Hockey',defaults={'name':'Jack'}) # one row it's satisfying(no error)
    # Webpage.objects.update_or_create(topic_name='Cricket',defaults={'name':'Jack'}) # (Cricket)more than one row satisfying(it will give error)
    # Webpage.objects.update_or_create(name='Messi', defaults={'topic_name':'WW'}) # error bcoz "topic_name" (we have to give value which present in parent table)
    
    # Webpage.objects.update_or_create(name='Messi', defaults={'topic_name':'WWE'}) # error bcoz "topic_name" (we have to give value which present in parent table as object)
    
    WTO=Topic.objects.get_or_create(topic_name = 'WWE')[0]      # here we got WWE object as WTO
    # Webpage.objects.update_or_create(name='Messi',defaults={'topic_name':WTO})  # updated WTO
    
    # Webpage.objects.update_or_create(name='CM_Punk',defaults={'topic_name':WTO})
    Webpage.objects.update_or_create(name='CM_Punk',defaults={'url':'http://punk.in'})
    Webpage.objects.update_or_create(name='CM_Punk',defaults={'url':'http://punk.com','email':'punk@gmail.com'})
    
    Webpage.objects.update_or_create(name='Randy_Ortan',defaults={'url':'http://randy.in','email':'ortan@gmail.com','topic_name':WTO})
    
    FTO = Topic.objects.get(topic_name='Football')
    Webpage.objects.update_or_create(name='Messi',defaults={'topic_name':FTO})
    

    QLWO = Webpage.objects.all()
    d = {'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def delete_webpage(request):
    
    # Webpage.objects.all().delete()   # this will delete all the records
    Webpage.objects.filter(name='Dhoni').delete()
    Webpage.objects.filter(name='Rohit').delete()
    
    QLWO = Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)






#--------AccessRecord
def display_accessrecord(request):
    QLARO=AccessRecord.objects.all()
    # QLARO=AccessRecord.objects.filter(id__gt=1)
    # QLARO=AccessRecord.objects.filter(id__gte=1)
    # QLARO=AccessRecord.objects.filter(id__lt=3)
    # QLARO=AccessRecord.objects.filter(id__lte=3)
    # QLARO=AccessRecord.objects.filter(author__startswith='b')
    # QLARO=AccessRecord.objects.filter(author__endswith='i')
    # QLARO=AccessRecord.objects.filter(date__year='2002')  
    # QLARO=AccessRecord.objects.filter(date__month='2')
    # QLARO=AccessRecord.objects.filter(date__day='31')
    # QLARO=AccessRecord.objects.filter(date__year__gt='2000')
    # QLARO=AccessRecord.objects.filter(date__year__lt='2000')
    
    
    # QLARO=AccessRecord.objects.filter(pk__in=[2,6])
    
    
    d={'accessrecord':QLARO}
    return render(request,'display_accessrecord.html',d)






def insert_accessrecord(request):
    n=input('Enter name: ')
    a=input('Enter author: ')
    d=input('Enter date: ')
    WO=Webpage.objects.get(name=n)
    ARO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    ARO.save()
    
    QLARO=AccessRecord.objects.all()
    d={'accessrecord':QLARO}
    return render(request,'display_accessrecord.html',d)
    
    