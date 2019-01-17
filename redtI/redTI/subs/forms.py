from django import forms
from .models import Thread, Post

class CreateaThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title']

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = forms.CharField()
        self.fields['post'] = field

    def save(self):
        post_content = self.cleaned_data['post']
        self.instance.subrediti_id = self.initial['subrediti'].id
        self.instance.authro = self.initial['author']
        self.instance.save()
        Post.objects_create(
            content = post_content, 
            author = self.instance.author, 
            thread = self.instance
        )
        return super().save()