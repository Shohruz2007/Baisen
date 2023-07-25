from django.db import models

from user.models import CustomUser

class GroupConversation(models.Model):
    theme = models.CharField(max_length=60)
    initiator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='group_initiator')
    start_time = models.DateTimeField(auto_now_add=True)


class PrivateConversation(models.Model):
    initiator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='private_initiator')
    reciever = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='private_reciever')
    start_time = models.DateTimeField(auto_now_add=True)


class GroupMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='group_message_sender')
    text = models.CharField(max_length=200, blank=True)
    attachment = models.FileField(blank=True)
    conversation = models.ForeignKey(GroupConversation, on_delete=models.CASCADE,)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)


class PrivateMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='private_message_sender')
    text = models.CharField(max_length=200, blank=True)
    attachment = models.FileField(blank=True)
    conversation = models.ForeignKey(PrivateConversation, on_delete=models.CASCADE,)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)