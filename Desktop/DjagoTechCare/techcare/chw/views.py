from django.shortcuts import render, redirect
from .models import Households
from .forms import HouseholdRegistrationForm
from django.contrib import messages


def addHousehold(request):

    if request.method == "POST":
        form = HouseholdRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Successfully registered' +
                             str(Households.contact_person_first_name))
            form.save()
            return redirect('household')
        else:
            print(form.errors)
    else:
        form = HouseholdRegistrationForm()
    return render(request, 'addhousehold.html', {'form': form})


def chwHouseholds(request):
    households = Households.objects.all()
    return render(request, 'household.html', {'households': households})


def edit_household(request, id):
    household = Households.objects.get(id=id)
    if request.method == 'POST':
        form = HouseholdRegistrationForm(request.POST, instance=household)
        if form.is_valid():
            form.save()
    else:
        form = HouseholdRegistrationForm(instance=household)
        return render(request, 'edit_household.html', {'form': form})


def assessments(request):
    return render(request, 'patient_assessments.html')


def referrals(request):
    return render(request, 'Referrals.html')


def followUp(request):
    return render(request, 'follow-up.html')

def new_household(request):
    return render(request, 'new_household.html')

def general_assessment(request):
    return render(request,'general_assessment.html')

def child_assess(request):
    return render(request,'child_assess.html')


def mother_assess(request):
    return render(request,'mother_assess.html')