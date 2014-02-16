from django.db import models

class client(models.Model):
    client_name = models.CharField(max_length=100)
    ach_payment_info = models.IntegerField(max_length=17)
    site_name = models.CharField(max_length=100)
    account_uname = models.CharField(max_length=100)
    account_password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.client_name

