from django import forms
from tinymce.widgets import TinyMCE
from blog.models import *

class PostForm(forms.ModelForm):
	tag = forms.MultipleChoiceField()		
	class Meta:
		model = Post
		exclude = ('user','created', 'modified', 'tags')
        widgets = {
            'content': TinyMCE(attrs={'cols': 20, 'rows': 10, 'class':'comment_text'}),
        }
        
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ('commenter','parent', 'modified', 'created','upvotes','downvotes')
        widgets = {
            'content': TinyMCE(attrs={'cols': 20, 'rows': 10, 'class':'comment_text'}),
        }

                