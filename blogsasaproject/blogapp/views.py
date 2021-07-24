

from django.db.models import Q


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, DetailView, ListView
from django.contrib import messages


from .forms import SaveAccount,SaveJob1, SaveJobs
from .models import Job, Account


# Create your views here

def Home(request):
    home= Job.objects.all
    return render(request, 'home.html', { 'home':home})

def save_job(request):
        # if this is a POST request we need to process the form data
    query = request.GET.get('q')
    if query:
        return querycategory(request)
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
        form = SaveAccount(request.POST)
            # check whether it's valid:
        if form.is_valid():
            form.save()
            form = SaveAccount()
            msg = 'Record saved successfully'
            print('OK')
            # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
            return render(request, 'post.html', {'form': form, 'msg': msg})
        else:
            form = SaveJob()
            print('NOT OK')

            return render(request, 'post.html', {'form': form})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = SaveJob
        return render(request, 'post.html', {'form': form})


class Register(CreateView):
    model = Account
    form_class = SaveAccount
    template_name = 'register.html'
    #success_url = reverse_lazy('register')



class SaveJob(CreateView):
    model = Job
#    form_class = SaveJob
    template_name = 'post.html'


def PostView(request, pk):
    category_posts = Job.objects.filter(id=pk)
    query = request.GET.get('q')
    if query:
        return querycategory(request)
    else:
        dict={ 'category_posts':category_posts}
        dict.update(querysidemenu(request))
        return render(request, 'postdetail.html',dict )

def CategoryView(request, cats):
    category_posts= Job.objects.filter(category= cats)
    cats1=cats.capitalize()
    query = request.GET.get('q')
    if query:
        return querycategory(request)
    else:
        dict = {'category_posts': category_posts}
        dict.update(querysidemenu(request))
        return render(request, 'category.html', dict)

def get_queryset(request):
    saveemail(request)
    query = request.GET.get('q')
    #count categories
    engineering = Job.objects.filter(category='engineering').count()
    banking = Job.objects.filter(category='banking').count()
    customerservice = Job.objects.filter(category='customer service').count()
    medical = Job.objects.filter(category='medical').count()
    softwareengineering = Job.objects.filter(category='software engineering').count()
    internship = Job.objects.filter(category='internship').count()
    agriculture = Job.objects.filter(category='agriculture').count()
    administration = Job.objects.filter(category='administration').count()
    driving = Job.objects.filter(category='driving').count()
    consultancy = Job.objects.filter(category='consultancy').count()
    catering = Job.objects.filter(category='catering').count()
    teaching = Job.objects.filter(category='teaching').count()
    marketing = Job.objects.filter(category='marketing').count()
    sales = Job.objects.filter(category='sales').count()
    procurement = Job.objects.filter(category='procurement').count()
    art = Job.objects.filter(category='art').count()
    legal = Job.objects.filter(category='legal services').count()
    humanresource = Job.objects.filter(category='human resource').count()
    if query:
        home= Job.objects.filter(position__icontains=query)
    else:
        home= Job.objects.filter(paid ='True')
    return render(request, 'home.html', {'home': home,'engineering': engineering,'banking': banking, 'customerservice': customerservice,'medical': medical, 'internship': internship,'agriculture': agriculture, 'administration': administration, 'driving': driving, 'consultancy': consultancy, 'catering': catering, 'softwareengineering': softwareengineering,'teaching': teaching,'marketing': marketing,'sales': sales, 'procurement': procurement, 'art': art, 'legal': legal,'humanresource': humanresource})

class SearchResultsView(ListView):
    model = Job
    template_name = 'home.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Job.objects.filter(position=query)
        return object_list


def save_form(request):
    # if this is a POST request we need to process the form data
    query = request.GET.get('q')
    if query:
        return querycategory(request)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SaveAccount(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = request.POST.get('email')
            if email:
                # check if the email already exists
                exists = Account.objects.filter(email=email).count()
                if exists < 1:
                    form.save()
                    form = SaveAccount()
                    msg = 'Record saved successfully'
                    return render(request, 'register.html', {'form': form, 'msg': msg})
                else:
                    error='Email already exists'
                    return render(request, 'register.html', {'form': form, 'error': error})

        else:
            form = SaveAccount()
            print('NOT OK')

            return render(request, 'register.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SaveAccount()
    return render(request, 'register.html', {'form': form})

def querycategory(request):
    engineering = Job.objects.filter(category='engineering').count()
    banking = Job.objects.filter(category='banking').count()
    customerservice = Job.objects.filter(category='customer service').count()
    medical = Job.objects.filter(category='medical').count()
    softwareengineering = Job.objects.filter(category='software engineering').count()
    internship = Job.objects.filter(category='internship').count()
    agriculture = Job.objects.filter(category='agriculture').count()
    administration = Job.objects.filter(category='administration').count()
    driving = Job.objects.filter(category='driving').count()
    consultancy = Job.objects.filter(category='consultancy').count()
    catering = Job.objects.filter(category='catering').count()
    teaching = Job.objects.filter(category='teaching').count()
    marketing = Job.objects.filter(category='marketing').count()
    sales = Job.objects.filter(category='sales').count()
    procurement = Job.objects.filter(category='procurement').count()
    art = Job.objects.filter(category='art').count()
    legal = Job.objects.filter(category='legal services').count()
    humanresource = Job.objects.filter(category='human resource').count()
    query = request.GET.get('q')
    if query:
        home= Job.objects.filter(position__icontains=query)
        return render(request, 'home.html',
                  {'home': home, 'engineering': engineering, 'banking': banking, 'customerservice': customerservice,
                   'medical': medical, 'internship': internship, 'agriculture': agriculture,
                   'administration': administration, 'driving': driving, 'consultancy': consultancy,
                   'catering': catering, 'softwareengineering': softwareengineering, 'teaching': teaching,
                   'marketing': marketing, 'sales': sales, 'procurement': procurement, 'art': art, 'legal': legal,
                   'humanresource': humanresource})


def querysidemenu(request):
    engineering = Job.objects.filter(category='engineering').count()
    banking = Job.objects.filter(category='banking').count()
    customerservice = Job.objects.filter(category='customer service').count()
    medical = Job.objects.filter(category='medical').count()
    softwareengineering = Job.objects.filter(category='software engineering').count()
    internship = Job.objects.filter(category='internship').count()
    agriculture = Job.objects.filter(category='agriculture').count()
    administration = Job.objects.filter(category='administration').count()
    driving = Job.objects.filter(category='driving').count()
    consultancy = Job.objects.filter(category='consultancy').count()
    catering = Job.objects.filter(category='catering').count()
    teaching = Job.objects.filter(category='teaching').count()
    marketing = Job.objects.filter(category='marketing').count()
    sales = Job.objects.filter(category='sales').count()
    procurement = Job.objects.filter(category='procurement').count()
    art = Job.objects.filter(category='art').count()
    legal = Job.objects.filter(category='legal services').count()
    humanresource = Job.objects.filter(category='human resource').count()
    query = request.GET.get('q')
    menu= {'engineering': engineering, 'banking': banking, 'customerservice': customerservice,
                   'medical': medical, 'internship': internship, 'agriculture': agriculture,
                   'administration': administration, 'driving': driving, 'consultancy': consultancy,
                   'catering': catering, 'softwareengineering': softwareengineering, 'teaching': teaching,
                   'marketing': marketing, 'sales': sales, 'procurement': procurement, 'art': art, 'legal': legal,
                   'humanresource': humanresource}
    return menu


class MyFormView(CreateView):
    form_class = SaveJob1
    template_name = 'post.html'

    def post(self, request, *args, **kwargs):
        # if this is a POST request we need to process the form data
        query = request.GET.get('q')
        if query:
            return querycategory(request)
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = SaveJob()
            msg = 'Record saved successfully'
            # redirect to a new URL:
            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})



#save the email for job alerts
def saveemail(request):
    email = request.POST.get('email')
    if email:
        #check if the email already exists
        exists=Account.objects.filter(email=email).count()
        if exists<1:
            e = Account(email=email)
            e.save()


def save_jobpost(request):
    messages.success(request, 'Record saved successfully')
    # if this is a POST request we need to process the form data
    query = request.GET.get('q')
    if query:
        return querycategory(request)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SaveJobs(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form = SaveJobs()
            msg = 'Record saved successfully'
            return render(request, 'post.html', {'form': form, 'msg': msg})

        else:
            form = SaveJobs()
            print('NOT OK')

            return render(request, 'post.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        msg = 'Record saved successfully'
        form = SaveJobs()
    return render(request, 'post.html', {'form': form,'msg': msg})