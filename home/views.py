from django.shortcuts import render, redirect
from eye.models import Info, Stock
from django.db.models import Q

#Company Info
company_name = 'Aethega'


#Navbar
def home(request):
    page = "home"
    data = {
        "page": page,
        "company_name": company_name,
    }
    return render(request, 'home/home.html', data)



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



def search(request):
    q = request.GET["q"]
    if q != "":
        results = 0
        try:
            qUp = str(q).upper()
            Stock.objects.get(symbol=qUp)
            return redirect(f"stocks/{qUp}")
        except:
            if (q == ":all"):
                results = Info.objects.all().order_by("ticker")[:100]
            elif (":ticker" in q):
                q = q.replace(":ticker", "")
                results = Info.objects.filter(ticker__startswith=q).order_by("ticker")
                q = q + " [filter: ticker]"
            else:       
                results = Info.objects.filter(Q(ticker__startswith=q) |
                                            Q(longName__startswith=q) |
                                            Q(sector=q)).order_by("ticker")
        length = len(results)
        data = {
            'q': q, 
            'results': results,
            'length': length,
        }
        return render(request, "home/search.html", data)