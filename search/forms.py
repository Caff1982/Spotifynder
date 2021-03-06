from django import forms


class SearchForm(forms.Form):
    
    song_title = forms.CharField(label='Song search', max_length=100, required=False,
                                 widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Search by song name'}))


class OptionsForm(forms.Form):
    OPTIONS = (
        ('energy', 'Energy'),
        ('danceability', 'Danceability'),
        ('speechiness', 'Speechiness'),
        ('acousticness', 'Acousticness'),
        ('instrumentalness', 'Instrumentalness'),
        ('liveness', 'Liveness'),
        ('valence', 'Valence')
    )
    search_options = forms.MultipleChoiceField(label='Search options',
                                               help_text='Select which features you want to use',
                                               required=False,
                                               widget=forms.CheckboxSelectMultiple(
                                                            attrs={'checked': '',
                                                                   'class': 'form-group'}),
                                                choices=OPTIONS)