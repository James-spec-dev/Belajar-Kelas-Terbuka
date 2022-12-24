from django import forms

from .models import ModelPost

class PostForm(forms.ModelForm):
	class Meta:
		model = ModelPost
		fields = [
			'author',
			'judul',
			'body',
			'category',
		]

		labels = {
			'author':'Penulis',
		}

		widgets = {
			'judul':forms.TextInput(
					attrs = {
						'class':'form-control',
						'placeholder':'isi dengan judul',
					}
				),

			'author':forms.TextInput(
					attrs = {
						'class':'form-control',
						'placeholder':'isi dengan nama penulis',
					}
				),

			'body':forms.Textarea(
					attrs = {
						'class':'form-control',
					}
				),

			'category':forms.Select(
					attrs = {
						'class':'form-control',
					}
				),

		}