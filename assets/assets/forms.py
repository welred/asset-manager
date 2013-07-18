from django.forms import ModelForm
from assets.models import *
from django.template.loader import render_to_string
import django.forms as forms 


'''

Model forms. Keep 'em generic!

'''


class AssetForm(ModelForm):
    class Meta:
        model = Asset


class LocationForm(ModelForm):
    class Meta:
        model = Location


class MakeForm(ModelForm):
    class Meta:
        model = AssetMake


class ModelForm(ModelForm):
    class Meta:
        model = AssetModel


class CheckoutForm(ModelForm):
    class Meta:
        model = AssetCheckout
        exclude = ('in_date')


class CheckinForm(ModelForm):
    class Meta:
        model = AssetCheckout
        fields = ('in_date',)


class ImportFileForm(ModelForm):
    class Meta:
        model = ImportFile


modelForms = {
    'asset': AssetForm,
    'location': LocationForm,
    'make': MakeForm,
    'model': ModelForm,
    'checkout': CheckoutForm,
}

class SelectWithPop(forms.Select):

    def render(self, name, *args, **kwargs):
        html = super(SelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string("form/add-popup.html", {'field': name})
        return html+popupplus

class MultipleSelectWithPop(forms.SelectMultiple):

    def render(self, name, *args, **kwargs):
        html = super(MultipleSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string("form/add-popup.html", {'field': name})
        return html+popupplus