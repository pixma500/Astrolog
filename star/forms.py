from django.core.exceptions import ValidationError
from .models import Posts
#from django.forms import ModelForm, forms
from django import forms
from taggit.models import Tag

class DateInput(forms.DateInput):
    input_type = 'date'

class PostsForm(forms.models.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())


    def clean_tags(self):
        tags = self.cleaned_data['tags']
        if len(tags) > 3:
            raise ValidationError("Нужно выбрать три категории")
        return tags

    class Meta:
        model = Posts
        fields = ('size', 'tags', 'description','publish' ,'status')
        widgets = {'publish': DateInput(),}

