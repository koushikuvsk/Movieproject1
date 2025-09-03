from django import forms
from django.forms import ModelForm
from MovieApp.models import Movie



class MovieForm(forms.ModelForm):
	class Meta:
		model=Movie
		fields=['moviename','genre','releasedate','rating','trailer_link']
		widgets={
		    'moviename':forms.TextInput(attrs={'class':'form-control','placeholder':'enter movie name'}),
		    'genre':forms.TextInput(attrs={'class':'form-control','placeholder':'enter genre'}),
		    'releasedate':forms.TextInput(attrs={'class':'form-control','placeholder':'enter release-date'}),
		    'rating':forms.NumberInput(attrs={'class':'form-control','placeholder':'enter your rating'}),
		    'trailer_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtu.be/...'}),


            
		}
	