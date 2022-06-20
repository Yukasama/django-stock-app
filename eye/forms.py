from django.forms import ModelForm
from eye.models import Portfolio


class PortfolioForm(ModelForm):
    
    class Meta:
        model = Portfolio
        fields = ["name"]
        
    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "input", "placeholder": "Portfolio Name"})

