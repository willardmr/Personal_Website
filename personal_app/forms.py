import random
import django.forms as forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class SimpleModelForm(forms.ModelForm):


    class Meta:
        model = SimpleModel
        fields = ['value']
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'The above are database values',
            ),
            ButtonHolder(
                Submit('submit', 'Click Here!', css_class='button white')
            )
        )
        super().__init__(*args, **kwargs)
        self.helper.form_show_labels = False
        self.fields['value'].initial = random.randint(-100, 100)
