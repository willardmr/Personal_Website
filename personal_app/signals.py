from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SimpleModel
 
 
@receiver(post_save, sender=SimpleModel)
def simple_model_post_save_handler(sender, **kwargs):
	models = SimpleModel.objects.order_by('-pk').values_list('pk', flat=True)[:3]
	SimpleModel.objects.exclude(pk__in=models).delete()
 
 