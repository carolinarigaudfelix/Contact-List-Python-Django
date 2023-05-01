from django.shortcuts import render, get_object_or_404

from .models import Contact
# Define o que vai acontecer quando o usuário faz algo, acessar uma rota por exemplo

def list(request):
    list_contacts = Contact.objects.all()

    return render(request, 
                'base.html', 
                {'list': list_contacts}
                )

def show_contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)

    return render(request,
                "show_contact.html",
                {'contact': contact}            
    )
