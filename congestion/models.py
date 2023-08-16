from django.db import models


class Bus(models.Model):
    # 인원수
    peopleNumber = models.IntegerField()
    # 혼잡도
    congestion = models.FloatField()
    # 현재 시간대
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.peopleNumber
