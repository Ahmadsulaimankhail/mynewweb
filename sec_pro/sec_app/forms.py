from django import forms


class userform(forms.Form):
    bookId = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Book ID'}))
    bookname= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Book Name'}))
    author= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Author Name'}))
    publisher=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Publisher Name'}))
    publicationYear=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Publication Year'}))
    quantity=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Quantity '}))


# class lendform(forms.Form):
#     personId=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter  Member ID'}))
#     pname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter First Name'}))
#     lname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Last Name'}))
#     # issue_date=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Issue Date'}))
#     # return_date=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Return Date'}))
#     book_id=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Book ID'}))
#     book_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Book Name'}))
#     quant=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Quantity'}))
# issue_date = forms.DateField(
#     widget=forms.DateInput(attrs={'type': 'date'})
# )

# return_date = forms.DateField(
#     widget=forms.DateInput(attrs={'type': 'date'})
# )


class lendform(forms.Form):

    personId = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Member ID'}))

    pname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))

    lname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))

    book_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Book ID'}))

    book_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Book Name'}) )

    quant = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Quantity'}))

    issue_date = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'})  )

    return_date = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'}))

