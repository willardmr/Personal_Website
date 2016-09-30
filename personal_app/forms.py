import random
import django.forms as forms
from .models import SimpleModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class SimpleModelForm(forms.ModelForm):
    """
    Form to create a SimpleModel
    """
    class Meta:
        model = SimpleModel
        fields = ['value']

    def __init__(self, *args, **kwargs):
        """
        We include help text, a submit button and initialize the form
        with a random value
        """
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'The above are database values.',
                'value'
            ),
            ButtonHolder(
                Submit('submit', 'Click Here!', css_class='button white')
            )
        )
        super().__init__(*args, **kwargs)
        self.helper.form_show_labels = False
        self.fields['value'].initial = random.randint(-100, 100)