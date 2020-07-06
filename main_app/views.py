from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Driver
from .forms import FuelingForm







class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  success_url = '/cars/'

class CarUpdate(UpdateView):
  model = Car
  # Let's disallow the renaming of a car by excluding the name field!
  fields = ['make', 'description', 'year']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /0ᐠ|||ᐟ0\</h1>')

def about(request):
  return render(request, 'about.html')

# def cars_index(request):
#   return render(request, 'cars/index.html', { 'cars': cars })

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  # Get the drivers the car doesn't have
  drivers_car_doesnt_have = Driver.objects.exclude(id__in = car.drivers.all().values_list('id'))
  # instantiate FuelingForm to be rendered in the template
  fueling_form = FuelingForm()
  return render(request, 'cars/detail.html', {
    # include the car and fueling_form in the context
    'car': car, 'fueling_form': fueling_form,
    # Add the drivers to be displayed
    'drivers': drivers_car_doesnt_have
  })

def add_fueling(request, car_id):
  # create a ModelForm instance using the data in request.POST
  form = FuelingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the car_id assigned
    new_fueling = form.save(commit=False)
    new_fueling.car_id = car_id
    new_fueling.save()
  return redirect('detail', car_id=car_id)

def assoc_driver(request, car_id, driver_id):
  Car.objects.get(id=car_id).drivers.add(driver_id)
  return redirect('detail', car_id=car_id)

def unassoc_driver(request, car_id, driver_id):
  Car.objects.get(id=car_id).drivers.remove(driver_id)
  return redirect('detail', car_id=car_id)

class DriverList(ListView):
  model = Driver

class DriverDetail(DetailView):
  model = Driver

class DriverCreate(CreateView):
  model = Driver
  fields = '__all__'

class DriverUpdate(UpdateView):
  model = Driver
  fields = ['name', 'skill']

class DriverDelete(DeleteView):
  model = Driver
  success_url = '/drivers/'