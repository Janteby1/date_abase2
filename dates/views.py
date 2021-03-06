from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import AddDateForm, SearchDateForm, UserForm, SearchDateForm_Area, SearchDateForm_Price
from .models import UserProfile, Dates 


# Create your views here.
class Index(View):
    def get(self, request):
        # create blank conext incase someone isnt signed in already 
        context = {}
        # check to see if someone is already logged in
        if request.user.is_authenticated(): 
            # get their username  
            username = request.user.username
            message = ("Hello, " + username)
            # send them a greating so they know they are signed in 
            context = {
                'message': message,}

        # this line gets all the posts that we have in the db and orders them by most recent
        dates = Dates.objects.filter(show=True).order_by('-count')[:15]
        # put all the dates into a context dict
        context ["dates"] = dates

        # send them all to the template
        return render(request, "dates/index.html", context)


class About(View):
    def get(self, request):
        return render(request, "dates/about.html")
        

class User_Register(View):
    # pu.db
    template = "dates/register.html"

    def get(self, request):
        "get the user form from forms.py and send it to the template in the context"
        user_form = UserForm()
        context = {
            'user_form': user_form,}
        return render(request, self.template, context)

    def post(self, request):
        user_form = UserForm(data=request.POST)
        # If the form is valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.save()
            # return render(request, "blog/index.html", {})
            return redirect("dates:index")

        else:
            context = {
                'user_form': user_form,}
            # send the form back with errors atatched 
            return render(request, self.template, context)


class User_Login(View):
    template = "dates/login.html"

    def get(self, request):
        # if the user is already signed in 
        if request.user.is_authenticated():
            return redirect("dates:index")
        return render(request, self.template, {})

    def post(self, request):
        # Gather the username and password entered by the user.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's to see if the username/password combination is valid, returns user object
        user = authenticate(username=username, password=password)

        if user: # meaning it is not None
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                login(request, user) 
                # send them back to the index and show them as logged in there
                return redirect("dates:index")
            else:
                # An inactive account was used
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided
            # print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")


class User_Logout(View):
    def get(self, request):
        # Since we know the user is logged in, we can now just log them out.
        logout(request)
        # Take the user back to the homepage.
        return redirect("dates:index")


class AddDate(View):
    # pu.db
    template = "dates/add.html"

    def get(self, request):
        form = AddDateForm()
        context = {
            'add_date_form': form,}
        return render(request, self.template, context)

    def post(self, request):
        # checks to make sure the user is logged in 
        if not request.user.is_authenticated():
            return HttpResponseForbidden(render (request, "403.html"))

        form = AddDateForm(data=request.POST)
        if form.is_valid():
            # add the user to each post 
            user = request.user
            date = form.save(commit=False)
            date.user = user
            date.save()
            return redirect("/")

        else:
            context = {
                'add_date_form': form,}
            return render(request, self.template, context)


class SearchDate(View):
    template = "dates/search.html"

    def get(self, request):
        form = SearchDateForm()
        context = {
            'search_date_form': form,}
        return render(request, self.template, context)

    # need to pass the check box values to the db and retun the date ideas
    def post(self, request):
        form = SearchDateForm(data=request.POST)
        if form.is_valid():

            # this gets all the values the user checked
            codes =(request.POST.getlist("category_choice"))

            # this returns a list of all the date ideas returned from the db 
            dates = Dates.objects.filter(category__in=codes)
            context = {
            'dates': dates,}
            return render(request, "dates/results.html", context)

        else:
            return HttpResponseForbidden(render (request, "403.html"))


class SearchDate_Area(View):
    template = "dates/search_area.html"

    def get(self, request):
        form = SearchDateForm_Area()
        context = {
            'search_date_form_area': form,}
        return render(request, self.template, context)

    # need to pass the check box values to the db and retun the date ideas
    def post(self, request):
        form = SearchDateForm_Area(data=request.POST)
        if form.is_valid():

            # this gets all the values the user checked
            codes =(request.POST.getlist("area_choice"))

            # this returns a list of all the date ideas returned from the db 
            dates = Dates.objects.filter(area__in=codes)
            context = {
                'dates': dates,}
            return render(request, "dates/results.html", context)

        else:
            return HttpResponseForbidden(render (request, "403.html"))


class SearchDate_Price(View):
    template = "dates/search_price.html"

    def get(self, request):
        form = SearchDateForm_Price()
        context = {
            'search_date_form_price': form,}
        return render(request, self.template, context)

    # need to pass the check box values to the db and retun the date ideas
    def post(self, request):
        form = SearchDateForm_Price(data=request.POST)
        if form.is_valid():

            # this gets all the values the user checked
            codes =(request.POST.getlist("price_choice"))

            # this returns a list of all the date ideas returned from the db 
            dates = Dates.objects.filter(price__in=codes)
            context = {
                'dates': dates,
            }
            return render(request, "dates/results.html", context)

        else:
            return HttpResponseForbidden(render (request, "403.html"))


class DateDetails(View):
    def get(self, request, dates_slug=None):
        # if we just want an ajax request we dont need a seperate class 
        if request.is_ajax():
            pk=request.GET.get("date_id")
            # do all the logic and filtering here, only get the comments that are shown and have the right id 
            dates = Dates.objects.filter(id=pk,show=True)

            # you need to save the value bc .filter is only a query set, not a bunch of objects
            date = dates[0]
            # this adds one to the count every time someone views the details to keep track of the "top dates"
            date.count += 1
            date.save()
            print (date.count) 

            # put all the values into a json dictionary with a method called from the models
            dates = [date.to_json() for date in dates]
            # put all the commentss into a context dict
            data = {
                "dates": dates }
            return JsonResponse(data) # return a json object to the ajax request


class Edit_Date(View):
    template = "dates/edit.html"

    # here we get the slug id passed in with the url 
    def get(self, request, dates_slug=None):
        if request.user.is_authenticated():
            date = Dates.objects.get(slug=dates_slug) 
            if request.user == date.user:
                # get the form and populate it with the value that is already there, AKA what we want to edit
                form = AddDateForm(instance=date)
                context = {
                    "date": date,
                    "EditForm": form }
                return render(request, self.template, context)
            else: 
                return HttpResponseForbidden(render (request, "403.html"))
        else: 
            return HttpResponseForbidden(render (request, "403.html"))

    def post(self, request, dates_slug=None):
        date = Dates.objects.get(slug=dates_slug) 
        form = AddDateForm(data=request.POST, instance=date)

        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            context = {
                "date": date,
                "EditForm": form,}
            # if it is not valid just send it back with the errors attached
            return render(request, self.template, context)


class Delete_Date(View):
    # dont need a get just get the slug id and change the value for show
    def post(self, request, dates_slug=None):

        date = Dates.objects.get(slug=dates_slug)
        # dont earase it just make the show field false so it wont show on index page
        date.show = False
        date.save()
        return redirect("/login")


class TopDate(View):
    # just want to send them to the results page with the one date they clicked as the context
    # dont need a get just get the slug id and change the value for show
    def get(self, request, dates_slug=None):
        date = Dates.objects.filter(slug=dates_slug)
        context = {
        'dates': date,}
        return render(request, "dates/results.html", context)


