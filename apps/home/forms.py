from django  import forms
from django import forms
from .models import *

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ('amount','deposit_address',)

class NftForm(forms.ModelForm):
    class Meta:
        model = Nft
        fields = ('image','title','price','currency','category','creator','description','owner','minted_by','on_display','is_featured','resolution','image_type','contract_address','token_id','blockchain_link',)

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = NewCategory
        fields = ('name','icon','email','description',)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name','email','description',)