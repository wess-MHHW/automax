from importlib import reload
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from main.filters import ListingFilter
from main.forms import ListingForm
from main.models import Listing
from users.forms import LocationForm

# Create your views here.
def main_view(request):
    return render(request,'views/main.html',{'name':"Automax"})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    context = {
        'listing_filter':listing_filter
    }
    return render(request,'views/home.html',context)

@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('home')
            else:
                raise Exception()
        except Exception as e:
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form': location_form, })

@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
    except Exception as e:
        messages.error(request, f'An invalid uuid {id} has been proven for')
        return redirect('home')
    return render(request, 'views/listing.html', {'listing':listing})

@login_required
def edit_view(request,id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        
        if request.method == 'POST':
            listing_form = ListingForm(request.POST,request.FILES,instance=listing)
            location_form = LocationForm(request.POST,instance=listing.location)
        
            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.success(request,'Listing updated successfully.')
                return redirect('home')
            else:
                messages.error(request,'Error updating listing.') 
                return reload()

        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
            context = {"listing_form":listing_form,'location_form':location_form}
    except Exception as e:
        messages.error(request,f'An error occured while updating the listing.')
    return render(request, 'views/edit.html', context)
