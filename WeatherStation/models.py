from django.db import models

# Create your models here.
class Record(models.Model):
    timeStamp = models.DateTimeField()
    recordNum = models.IntegerField(primary_key=True)
    battAvg = models.DecimalField(max_digits=4,decimal_places=2)
    pTempCAvg = models.DecimalField(max_digits=4,decimal_places=2)
    airTCAvg = models.DecimalField(max_digits=4,decimal_places=2)
    rH = models.DecimalField(max_digits=4,decimal_places=2)
    slrkW = models.DecimalField(max_digits=4,decimal_places=2)
    slrMJTot = models.DecimalField(max_digits=8,decimal_places=6)
    wSMs = models.DecimalField(max_digits=6,decimal_places=3)
    windDir = models.DecimalField(max_digits=5,decimal_places=1)
    pARDen = models.DecimalField(max_digits=5,decimal_places=1)
    pARTotTot = models.DecimalField(max_digits=10,decimal_places=2)
    bPMmHg = models.DecimalField(max_digits=6,decimal_places=1)
    rainMmTot = models.IntegerField()

    class Meta:
        ordering = ['-recordNum']
        managed = True

    def __str__(self):
        return self.recordNumlo