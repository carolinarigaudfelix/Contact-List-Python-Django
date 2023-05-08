from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import MyForm
from django.http import HttpResponse
# Define o que vai acontecer quando o usuário faz algo, acessar uma rota por exemplo

def show_contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)
    print(contact)
    if request.method == 'POST':
        #name = request.POST.get('name')
        form = MyForm(request.POST, request.FILES,instance=contact)

        # if name: # Verifica se o campo name está preenchido
            # contact.image = request.POST.get('image')
            # contact.name = request.POST.get('name')
            # contact.email = request.POST.get('email')
            # contact.phone = request.POST.get('phone')
            # contact.save()
        form.save()
        return redirect('show_contact', id_contact=id_contact)
        # else:
            # Caso contrário, retorna uma mensagem de erro ou renderiza um template com uma mensagem de erro
        return HttpResponse("O campo nome é obrigatório")

       
    return render(request, 'show_contact_new.html', {'contact': contact, 'id_contact': id_contact})

def contact_list(request):
    list_contacts = Contact.objects.all()
    
    return render(request, 
                'base.html', 
                {'contact_list': list_contacts}
                )


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
    
    return render(request,
                  "edit_contact.html",
                  {'contact': contact, 'id_contact': id_contact}
            )



