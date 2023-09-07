from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    FORBIDDEN_WORDS = {
        'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('slug', 'create_date', 'modify_date', 'count_views')

    def clean_name(self):
        cleaned_data = set(str(self.cleaned_data.get('name')).split())
        intersection = cleaned_data.issubset(self.FORBIDDEN_WORDS)
        if intersection:
            raise forms.ValidationError('Ошибка в name')

        return self.cleaned_data.get('name')

    def clean_description(self):
        cleaned_data = set(str(self.cleaned_data.get('description')).split())
        intersection = cleaned_data.issubset(self.FORBIDDEN_WORDS)
        if intersection:
            raise forms.ValidationError('Ошибка в description')

        return self.cleaned_data.get('description')


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
