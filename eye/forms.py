from django.forms import ModelForm
from eye.models import Portfolio




class PortfolioForm(ModelForm):
    
    class Meta:
        model = Portfolio
        fields = ["portf_name"]

