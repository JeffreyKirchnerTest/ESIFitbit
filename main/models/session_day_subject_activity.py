from django.db import models
import logging
import traceback
from django.utils.timezone import now
from . import Session_day,Session_subject
import uuid

from enum import Enum

#one day from session 
class Session_day_subject_actvity(models.Model):
    session_day = models.ForeignKey(Session_day,on_delete=models.CASCADE)
    session_subject = models.ForeignKey(Session_subject,on_delete=models.CASCADE,related_name="Session_day_subject_actvities")

    heart_activity_minutes = models.DecimalField(decimal_places=10, default=0, max_digits=20)       #todays heart activity minutes
    immune_activity_minutes = models.DecimalField(decimal_places=10, default=0, max_digits=20)      #todays immune activity minutes

    heart_activity = models.DecimalField(decimal_places=10, default=0, max_digits=20)               #todays heart activity calculation
    immune_activity = models.DecimalField(decimal_places=10, default=0, max_digits=20)              #todays immune activity calculation
    
    check_in_today = models.BooleanField(default=False)                                             #true if the user checked in today
    paypal_today = models.BooleanField(default=False)                                               #true if the user collected their payment today

    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)

    def __str__(self):
        return "Period " + str(self.session_day.period_number) + " Subject " + self.session_subject
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['session_day', 'session_subject'], name='unique_SDSA')
        ]
        verbose_name = 'Session Day'
        verbose_name_plural = 'Session Days'

    #calc heart activity
    def calcHeartActivity(self,heart_time,heartActivityMinus1):
        p_set = self.session_day.session.parameterset

        self.heart_activity = self.calcActivity(heart_time,
                                                p_set.heart_parameter_1,
                                                p_set.heart_parameter_2,
                                                p_set.heart_parameter_3,
                                                heartActivityMinus1)

        self.save()

    #calc immune activity
    def calcImmuneActivity(self,immune_time,immuneActivityMinus1):
        p_set = self.session_day.session.parameterset

        self.immune_activity= self.calcActivity(immune_time,
                                                p_set.immune_parameter_1,
                                                p_set.immune_parameter_2,
                                                p_set.immune_parameter_3,
                                                immuneActivityMinus1)
        
        self.save()

    #calc activity
    def calcActivity(self,active_time,p1,p2,p3,activityMinus1): 
        #immuneActivityTodayT-1 * (1 - (1 - immuneActivityTodayT-1) * (immune_parameter_1 / immune_parameter_2  - immuneTimeT-1 / (immuneTimeT-1 + immune_parameter_3))

        return activityMinus1 * (1 - (1 - activityMinus1) * (p1 / p2  - active_time / (active_time + p3)))     

    #return json object of class
    def json(self):
        return{
            "id":self.id,
            "treatment":self.treatment,           
        }