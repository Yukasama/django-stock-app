from django.shortcuts import render



def help(response):
    return render(response, 'support/help.html')
