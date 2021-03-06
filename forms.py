from django import forms as newforms
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
import cPickle as pickle



#text field for everything, Height(cm): Height, Weight(kg): Weight
class Add_Document(newforms.Form):
	#height = newforms.IntegerField(initial=210,required = True)
	#weight = newforms.FloatField(initial=120, required = True)
	#vitals_circumstance = newforms.CharField(max_length = 100, initial = "Enter a circumstance")
	#vitals_item = newforms.CharField(max_length=6, widget=widgets.Select(choices = ITEM_CHOICES))
	#namespace = newforms.CharField(required = True, label = "Namespace")
	doc_name = newforms.CharField(label="Document Name",widget=newforms.widgets.TextInput(attrs={'class':"text ui-widget-content ui-corner-all", 
		'id':'doc_name'}))
	#For some reason, you can't set the name using the attributes.
	#namespace is not being used because it is being added dynamically by JQUERY.
	#namespace = newforms.CharField(label="Namespace(s)",widget=newforms.widgets.TextInput(attrs={'class':"text ui-widget-content ui-corner-all", 
		#'id':'namepace','html-name':'namespace-1'}))
	
	#def clean_namespace(self):
		#try:
		#	
		#except:
		#	return self.cleaned_data['namespace']
		#raise forms.ValidationError(u'This namespace is not valid. Please use the appropriate syntax')

#class RegistrationForm(forms.Form):
 #   username = forms.CharField(max_length=30)
  #  email = forms.EmailField()
   # password = forms.CharField()
    
   # def clean_username(self):
   #     try:
   #         user = User.objects.get(username=self.cleaned_data['username'])
   #     except User.DoesNotExist:
   #         return self.cleaned_data['username']
   #     raise forms.ValidationError(u'This username is already taken. Please choose another.


"""
Copyright 2011 Health Records for Everyone

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
