from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
        else:
            form = EmployeeForm()
        return render(request, 'index.html', {'form': form})

    else:
        form = EmployeeForm(request.GET)
        return render(request, 'index.html', {'form': form})


def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html', {'employee': employee})


def edit(request, id):
    employee = Employee.objects.get(Eid=id)
    return render(request, 'edit.html', {'employee': employee})


def delete(request, id):
    employee = Employee.objects.get(Eid=id)
    employee.delete()
    return redirect("/show")


def update(request, id):
    employee = Employee.objects.get(Eid=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    # return redirect('/show')
    # else:
    #     form = EmployeeForm(request.GET)
    #     return render(request,'edit.html',{'form':form})
#     return render(request,'edit.html',{'form':form})


# def update(request, Eid):
#     # Get the employee object based on the Eid
#     employee = Employee.objects.get(Eid=Eid)
#
#     # Check if the form has been submitted (POST method)
#     if request.method == "POST":
#         # Create a form instance with POST data and the existing employee object
#         form = EmployeeForm(request.POST, instance=employee)
#
#         # Validate the form and save if valid
#         if form.is_valid():
#             form.save()  # Save the updated employee details
#             return redirect('/show')  # Redirect to the page showing the updated employee data
#
#     # If the request is a GET or the form is not valid, render the form with existing data
#     else:
#         form = EmployeeForm(instance=employee)
#
#     # Render the edit page with the form
#     return render(request, 'edit.html', {'form': form, 'employee': employee})

# def update(request, Eid):
#     employee = Employee.objects.get(Eid=Eid)
#
#     # If the request is a POST, we are trying to update the employee data
#     if request.method == "POST":
#         form = EmployeeForm(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()  # Save the updated employee details
#             return redirect('/show')  # Redirect to the show page after saving
#     else:
#         # If it's a GET request, we want to pre-populate the form with the existing data
#         form = EmployeeForm(instance=employee)
#
#     # Render the edit page with the form in case of both GET requests or invalid form
#     return render(request, 'edit.html', {'form': form})

# def update(request, Eid):
#     employee = Employee.objects.get(Eid=Eid)  # Fetch the employee object based on Eid
#
#     if request.method == 'POST':  # Check if the form is submitted
#         form = EmployeeForm(request.POST)
#         if form.is_valid():  # Validate the form
#             form.save()  # Save the updated data
#             return redirect('/show')  # Redirect after successful update
#         else:
#             # If the form is invalid, re-render the form with errors
#             form = EmployeeForm()
#             return render(request, 'edit.html', {'form': form})
#
#     # If the request is GET, display the form with existing data
#     else:
#         form = EmployeeForm(request.GET)
#         return render(request, 'edit.html', {'form': form})
# def update(request, Eid):
#     employee = Employee.objects.get(Eid=Eid)  # Fetch the employee object based on Eid
#
#     if request.method == 'GET':  # Check if the form is submitted
#         form = EmployeeForm(request.GET, instance=employee)
#         if form.is_valid():  # Validate the form
#             form.save()  # Save the updated data
#             return redirect('/show')  # Redirect after successful update
#         else:
#             # If the form is invalid, re-render the form with errors
#             return render(request, 'edit.html', {'form': form, 'employee': employee})
#
#     # If the request is GET, display the form with existing data
#     else:
#         form = EmployeeForm(instance=employee)
#         return render(request, 'edit.html', {'form': form, 'employee': employee})
