from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Contact
from .forms import MyForm


def index(request):
    contacts = Contact.objects\
        .order_by('-id')
    
    context = {
        'contacts':contacts,
        'site_title': 'Contact List'
    }

    return render(
        request, 
        'contact_list'
    )


def show_contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)
    print(contact)
    if request.method == 'POST':

        form = MyForm(request.POST, request.FILES,instance=contact)
        form.save()
        return redirect('show_contact', id_contact=id_contact)

    
    return render(request, 'show_contact_new.html', {'contact': contact, 'id_contact': id_contact})

def contact_list(request):
    txt_name = request.GET.get('name')
    if txt_name:
        contacts = Contact.objects.filter(name__icontains=txt_name)
        paginator = Paginator(contacts, 4)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    else:
        contacts = Contact.objects.all()
        paginator = Paginator(contacts, 4)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    
        
    context = {
        'contact_list': page_obj,
        'txt_name': txt_name,
    }
    
    return render(request, 'base.html', context)




def new_contact(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
    
            form.save()
            return redirect('contact_list')
    else:
        form = MyForm()
    return render(request, 'new_contact.html', {'form': form})


def edit_contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)
    
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('show_contact', id_contact=id_contact)
    else:
        form = MyForm(instance=contact)

    context = {'contact': contact, 'id_contact': id_contact, 'form': form}
    return render(request, "edit_contact.html", context)

def delete_contact(request, id_contact): 
    contact = get_object_or_404(Contact, id=id_contact)
    contact.delete()

    if request.method == 'POST':
        return redirect('contact_list')
    
    return render(request, 'show_contact_new.html', {'contact': contact, 'id_contact': id_contact})


