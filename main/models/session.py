from django.db import models
import logging
import traceback
from django.utils.timezone import now
from . import Parameterset

from django.dispatch import receiver
from django.db.models.signals import post_delete
import main
import pytz

from main.models import Parameters

from datetime import datetime,timedelta

from enum import Enum
from django.utils.translation import gettext_lazy as _
   
#experiment sessoin
class Session(models.Model):

    class Treatment(models.TextChoices):
        ONE = 'I', _('Individual')
        TWO = "IwC", _('Individual with chat')
        THREE = "IwCpB", _('Individual with chat and bonus')

    parameterset = models.ForeignKey(Parameterset,on_delete=models.CASCADE)

    title = models.CharField(max_length = 300,default="*** New Session ***")    #title of session
    start_date = models.DateField(default=now)                                  #date of session

    treatment = models.CharField( max_length=100, choices=Treatment.choices,default=Treatment.ONE)    

    soft_delete =  models.BooleanField(default=False)                            #hide session if true

    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Experiment Session'
        verbose_name_plural = 'Experiment Sessions'

    #get the current session day
    def getCurrentSessionDay(self):
        logger = logging.getLogger(__name__)

        return self.session_days.order_by('-period_number').first()

    #add new sessions days up to today if needed
    def addNewSessionDays(self):
        logger = logging.getLogger(__name__)
        logger.info("Add new sessions: " + str(self.title))

        #get today's date
        p = Parameters.objects.first()
        tz = pytz.timezone(p.experimentTimeZone)
        d_today = datetime.now(tz)
        d_today = d_today.replace(hour=0,minute=0, second=0,microsecond=0)

        sd = self.session_days.order_by('-date').first()
        logger.info(sd.date)
        logger.info(d_today.date())

        while sd.date < d_today.date():
            logger.info("Newest session day: " + str(sd))
            
            d_temp = datetime.now(tz)
            d_temp = d_today.replace(hour=0,minute=0, second=0,microsecond=0)
            d_temp = d_today.replace(day=sd.date.day,month=sd.date.month, year=sd.date.year)
            
            d_temp += timedelta(days=1)

            #logger.info(d_temp.date())

            self.addSessionDay(d_temp.date(),sd.period_number+1)    

            sd = self.session_days.order_by('-date').first()        

    #add new session day to this session
    def addSessionDay(self,new_day,new_period):
        logger = logging.getLogger(__name__)

        new_sd = main.models.Session_day()
        new_sd.date = new_day
        new_sd.session=self
        new_sd.period_number=new_period
        new_sd.save()

        new_sd.addSessionDayUserActivites()

        logger.info("Created session day: " + str(new_sd))

    #fill subjects with test data    
    def fillWithTestData(self):

        for s in self.session_subjects.all():
            s.fillWithTestData()


    #get user readable string of start session date
    def getDateString(self):
        return  self.start_date.strftime("%#m/%#d/%Y")

    #return json object of class
    def json(self):
        return{
            "id":self.id,
            "title":self.title,
            "start_date":self.getDateString(),
            "current_session_day":self.getCurrentSessionDay().json(),
            "treatment":self.treatment,
            "treatment_label":self.Treatment(self.treatment).label,
            "parameterset":self.parameterset.json(),
        }

#delete associated user model when profile is deleted
@receiver(post_delete, sender=Session)
def post_delete_parameterset(sender, instance, *args, **kwargs):
    if instance.parameterset: 
        instance.parameterset.delete()