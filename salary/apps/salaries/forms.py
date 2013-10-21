from django import forms
from haystack.forms import ModelSearchForm

class AutocompleteModelSearch(ModelSearchForm):
	def search(self):
		if not self.is_valid():
			return self.no_query_found()
		if not self.cleaned_data.get('q'):
			return self.no_query_found()
		sqs = self.searchqueryset.filter(name_auto=self.full_name)


class MugForm(forms.Form):
	mug = forms.ImageField(
		label='Select a file',	
    )


