from django import forms
from main.models import Session_subject_questionnaire1
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
import pytz
from main.globals.likertScales import Likert_importance,Likert_satisfaction,Likert_variation

class Session_subject_questionnaire1_form(forms.ModelForm):

    #sleep
    sleep_hours = forms.DecimalField(label='How many hours do you sleep in a typical night?',
                            min_value=0,
                            widget=forms.NumberInput(attrs={"value":0.0,"step":"0.1","min":0,"max":24}))
    
    sleep_importance = forms.TypedChoiceField(label='How important is it to you to get a good night’s sleep?', 
                                         choices=Likert_importance.choices,
                                         initial=Likert_importance.FOUR,                   
                                         widget=forms.Select(attrs={}))
    
    sleep_explanation = forms.CharField(label='Why?',
                                        widget=forms.Textarea(attrs={"rows":"5", "cols":"75"}))

    #exercise
    exercise_hours = forms.DecimalField(label='How many minutes do you exercise in a typical day?',
                            min_value=0,
                            widget=forms.NumberInput(attrs={"value":0.0,"step":"0.1","min":0,"max":24}))
    
    exercise_importance = forms.TypedChoiceField(label='How important is it to you to exercise?', 
                                         choices=Likert_importance.choices,
                                         initial=Likert_importance.FOUR,                   
                                         widget=forms.Select(attrs={}))
    
    exercise_explanation = forms.CharField(label='Why?',
                                        widget=forms.Textarea(attrs={"rows":"5", "cols":"75"}))

    #health importance
    health_importance = forms.TypedChoiceField(label='For you personally, how important is it to maintain your overall health? ', 
                                         choices=Likert_importance.choices,
                                         initial=Likert_importance.FOUR,                   
                                         widget=forms.Select(attrs={}))
    
    health_importance_explanation = forms.CharField(label='Why?',
                                        widget=forms.Textarea(attrs={"rows":"5", "cols":"75"}))
    
    health_importance_actions = forms.CharField(label='For you personally, what does maintaining your health include? ',
                                        widget=forms.Textarea(attrs={"rows":"5", "cols":"75"}))
    
    health_satisfaction = forms.TypedChoiceField(label='How satisfied are you with your current efforts to maintain your health?', 
                                         choices=Likert_satisfaction.choices,
                                         initial=Likert_satisfaction.FOUR,                   
                                         widget=forms.Select(attrs={}))

    sleep_variation = forms.TypedChoiceField(label='How much day to day variation is there in the amount of time you spend sleeping?', 
                                         choices=Likert_variation.choices,
                                         initial=Likert_variation.FOUR,                   
                                         widget=forms.Select(attrs={}))

    sleep_variation_explanation = forms.CharField(label='For you personally, what are the typical reasons that you might not get a good night’s sleep?',
                                        widget=forms.Textarea(attrs={"rows":"5", "cols":"75"}))

    exercise_variation = forms.TypedChoiceField(label='How much day to day variation is there in the amount of time you spend exercising?', 
                                         choices=Likert_variation.choices,
                                         initial=Likert_variation.FOUR,                   
                                         widget=forms.Select(attrs={}))

    exercise_variation_explanation = forms.CharField(label='For you personally, what are the typical reasons that you might not exercise daily?',
                                        widget=forms.Textarea(attrs={"rows":"5", "cols":"75"}))

    class Meta:
        model=Session_subject_questionnaire1
        exclude=['session_subject']