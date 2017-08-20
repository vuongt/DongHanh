from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, ButtonHolder, HTML, Div

from django.forms import ModelForm
from .models import University


class UniversityUpdateForm(ModelForm):
    class Meta:
        model = University
        fields = ['name', 'code', 'about']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-default submit'))

        super(UniversityUpdateForm, self).__init__(*args, **kwargs)

