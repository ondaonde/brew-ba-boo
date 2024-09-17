from django.forms import ModelForm
from main.models import Potion

class PotionForm(ModelForm):
    class Meta:
        model = Potion
        fields = ["name", "description", "caution", "price"]