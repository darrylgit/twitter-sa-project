from django import forms

class SearchForm(forms.Form):
	query_error_messages = {
		'required':'Try adding a query'
	}
	query = forms.CharField(error_messages=query_error_messages, required=True, label="Search", max_length=155)