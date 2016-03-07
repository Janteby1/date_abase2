from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import AddDateForm, SearchDateForm
from .models import UserProfile, Dates 

# Create your views here.
class Index(View):
    def get(self, request):
        # # this gets them all, eventually want to add hits and show the ones with the most hits
        # dates = Dates.objects.all().order_by('-created_at')
        # context = {
        #     'dates': dates, }
        return render(request, "dates/index.html")


class AddDate(View):
    # pu.db
    template = "dates/add.html"

    def get(self, request):
        form = AddDateForm()
        context = {
            'add_date_form': form,}
        return render(request, self.template, context)

    def post(self, request):
        form = AddDateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dates")

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
            pass
            # if nothing matches the search the HTML page will display 
            # a message and have a link back home or to search again 

