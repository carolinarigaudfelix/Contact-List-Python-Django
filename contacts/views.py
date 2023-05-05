from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.http import HttpResponse
# Define o que vai acontecer quando o usuário faz algo, acessar uma rota por exemplo

def contact_list(request):
    list_contacts = Contact.objects.all()
    
    return render(request, 
                'base.html', 
                {'contact_list': list_contacts}
                )

def show_contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name: # Verifica se o campo name está preenchido
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.phone = request.POST.get('phone')
            contact.save()
            return redirect('show_contact', id_contact=id_contact)
        else:
            # Caso contrário, retorna uma mensagem de erro ou renderiza um template com uma mensagem de erro
            return HttpResponse("O campo nome é obrigatório")
    else:
        {
            'name': contact.name,
            'email': contact.email,
            'phone': contact.phone,
            'category': contact.category,
        }
    return render(request, 'show_contact_new.html', {'contact': contact, 'id_contact': id_contact})


def edit_contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)

    return render(request,
                  "edit_contact.html",
                  {'contact': contact, 'id_contact': id_contact}
            )

def new_contact (request):
     return render(request, "new_contact.html", {})

def image_avatar(request):
    avatar = Contact.objects.all() # ou qualquer outro filtro
    return render(request,
                "_list_contacts.html",
                  {'avatar': avatar})
