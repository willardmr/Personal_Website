import json
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.core.serializers.json import DjangoJSONEncoder
from .forms import SimpleModelForm
from .models import SimpleModel


class AboutView(TemplateView):
    """
    Index page. Include model form.
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SimpleModelForm()
        context['form'] = form
        context['models'] = SimpleModel.objects.all()
        return context


@csrf_protect
def create_model(request):
    """
    Ajax view allowing javascript calls to create new
    SimpleModel objects
    """
    if request.method == 'POST':
        value = int(request.POST.get('the_post'))
        if value == '':
            value = 0
        # Django integerfield only allows values between these
        if value >= -2147483648 and value <= 2147483647:
            SimpleModel.objects.create(value=value)

        return HttpResponse(
            json.dumps(
                list(SimpleModel.objects.all().values_list('value',)),
                cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        raise Http404()
