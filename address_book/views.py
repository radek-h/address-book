from address_book.models import Person, Email, Phone
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import PersonForm, PhoneForm, EmailForm
from django.views.decorators.csrf import csrf_exempt


def contact_list(request):
    people = Person.objects.all()
    if (people.count() == 0):
        messages.info(request, "Wygląda na to, że twoja książka adresowa jest pusta. Dodaj jakieś kontakty :)")
    field_names = {'1':'Imię', '2':'Nazwisko', '3':'Telefon', '4':'Email', }
    return render(request,'address_book/main.html',
                  context={
                            'people': people,
                            'field_names': field_names,
                          })


def contact_search(request):
    radio_val = int(request.GET['rb'])
    search_val = request.GET['search']
    entire_contacts_button = True

    field_names = {'1': 'Imię', '2': 'Nazwisko', '3': 'Telefon', '4': 'Email', }
    if radio_val == 1: # po imieniu
        people = Person.objects.filter(first_name__icontains=search_val)
    elif radio_val == 2: # po nazwisku
        people = Person.objects.filter(last_name__icontains=search_val)
    elif radio_val == 3: # po numerze tel
        people = Person.objects.filter(phone__phone__icontains=search_val)
    elif radio_val == 4: # po mailu
        people = Person.objects.filter(email__email__icontains=search_val)

    if people.count() == 0:
        messages.error(request, f"Nie znaleziono wyników dla {search_val}")
        return redirect('address_book:contact_list')
    return render(request,'address_book/main.html',
                  context={
                      'people': people,
                      'field_names': field_names,
                      'entire_contacts_button': entire_contacts_button,
                })


@csrf_exempt
def contact_detail(request, pk):

    instance = get_object_or_404(Person, id=pk)

    if request.method == 'DELETE':
        instance.delete()
        return HttpResponse(status=204)

    elif request.method == 'POST':
        person_edit = PersonForm(request.POST or None, instance=instance)
        if person_edit.is_valid():
            person_edit.save()
        return HttpResponseRedirect('/')


def contact_add(request):
    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        phone_form = PhoneForm(request.POST)
        email_form = EmailForm(request.POST)

        if person_form.is_valid() and phone_form.is_valid() and email_form.is_valid():
            person = person_form.save()
            phone = phone_form.save(False)
            email = email_form.save(False)

            phone.person = person
            email.person = person

            phone.save()
            email.save()
            messages.success(request, f"Dodano nowy kontakt: {request.POST['first_name']} {request.POST['last_name']}")
            return HttpResponseRedirect('/')

    else: # GET
        person_form = PersonForm()
        phone_form = PhoneForm()
        email_form = EmailForm()

    return render(request,
                  'address_book/add_contact.html',
                  {
                      'person_form':person_form,
                      'phone_form':phone_form,
                      'email_form':email_form,
                  })


@csrf_exempt
def phone_add(request, pk):

    instance = get_object_or_404(Person, id=pk)
    if request.method == "POST":
        phone_form = PhoneForm(request.POST)
        if phone_form.is_valid():
            phone = phone_form.save(False)
            phone.person_id = instance.id
            try:
                Phone.objects.get(phone__exact='', person_id=instance.id).delete()
            except Phone.DoesNotExist:
                pass
            phone.save()
            messages.success(request, f"Dodano nowy numer tel. {request.POST['phone']}")
        else:
            messages.error(request, f"Nie dodano poprawnie nr tel.")
        return redirect('address_book:contact_list')


@csrf_exempt
def email_add(request, pk):

    instance = get_object_or_404(Person, id=pk)
    if request.method == "POST":
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            email = email_form.save(False)
            email.person_id = instance.id
            try:
                Email.objects.get(email__exact='', person_id=instance.id).delete()
            except Email.DoesNotExist:
                pass
            email.save()
            messages.success(request, f"Dodano nowy mail: {request.POST['email']}")

        else:
            messages.error(request, f"Sprawdź czy wpisałeś poprawnie maila.")
        return redirect('address_book:contact_list')



