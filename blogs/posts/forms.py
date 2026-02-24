
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['post']
        widgets = {
        'comment': forms.Textarea(attrs={'class':'form-control','placeholder':'Add your comments here...'}),
    }

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = '__all__'
#         widgets = {
#             'tag': forms.Textarea(attrs={'class':'form-control','placeholder':'Add your tags here...'}),
#         }
