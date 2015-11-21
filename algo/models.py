from django.db import models


class StatusObject(models.Model):
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return '{} {}'.format(self.status, self.message)

    def toDict(self):
        return {
            "status":   self.status,
            "message": self.message,    
        }