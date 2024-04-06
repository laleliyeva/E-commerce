# from django.db.models import signals
# from django.contrib.auth import get_user_model
# # from django.db.models.signals import post_save #Import a post_save signal when a user is created
# # from django.contrib.auth.models import User # Import the built-in User model, which is a sender
# # from django.dispatch import receiver # Import the receiver
# from .models import UserProfile

# User = get_user_model()


# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# signals.post_save.connect(create_profile ,  sender = User)