from django import forms
from core.models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text','image')