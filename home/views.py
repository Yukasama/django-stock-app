from django.shortcuts import render


#Company Info
company_name = 'Aethega'


#Navbar
def home(request):
    return render(request, 'home/home.html', 
        {'company_name': company_name, }
    )



#Footer
def aboutus(request):
    return render(request, 'home/aboutus.html')



def careers(request):
    return render(request, 'home/careers.html')



def faq(request):
    return render(request, 'home/faq.html')



def contact(request):
    mail = request.POST['mail']
    subject = request.POST['subject']
    message = request.POST['message']
    contactData = {
        'Mail': mail,
        'Subject': subject,
        'Message': message,
    }
    return render(request, 'home/contact.html', contactData)



def pricing(request):
    return render(request, 'home/pricing.html')
    
    
    
def development(request):
    return render(request, 'home/development.html')



def newsletter(request):
    return render(request, 'home/newsletter.html')



def terms(request):
    return render(request, 'home/terms.html')



def privacy(request):
    return render(request, 'home/privacy.html')