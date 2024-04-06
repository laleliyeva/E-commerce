from celery import shared_task
from core.models import Subscriber
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
from django.db.models import Count
from product.models import Product
from datetime import timedelta
from account.models import CustomUser






@shared_task
def send_mail_to_subscribers():
    startdate = timezone.now()
    enddate = startdate = timedelta(days=7)
    subscriber_emails = Subscriber.objects.values_list('email' , flat=True)
    most_rev = Product.objects.filter(created_at_gte = enddate).annotate
    product = most_rev.order_by('-created_time')[0:4]

    for mail in subscriber_emails:
        body = render_to_string('email-subscriber.html' , context={
            'email' : mail ,
            
        })  
        msg = EmailMessage(subject='Subscriber mail' , body=body,
                           from_email=settings.EMAIL_HOST_USER , 
                           to=[mail,])
        msg_content_subtype = 'html'
        msg.send(fail_silently=True)

