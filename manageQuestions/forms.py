from django import forms
from question.models import Question

# options 
DIFFICULTY = ((0, "Easy"), (1, "Medium"), (2, "Hard"), (3, "Insane"))
STATUS = ((0, "Save as draft"), (1, "Submit for approval"))

# form
class QuestionCreateForm(forms.ModelForm):
    """
    form for creating a question
    """
    title = forms.CharField(label="Title", max_length=100)
    summary = forms.CharField(label="Summary", max_length=200)
    content = forms.CharField(label="Content", widget=forms.Textarea)
    difficulty = forms.ChoiceField(choices=DIFFICULTY, label="Difficulty")
    approved = forms.ChoiceField(choices=STATUS, label="Save or Submit?")

    # add classes for styling
    title.widget.attrs.update({"placeholder": "Title"})
    summary.widget.attrs.update({"placeholder": "Summary"})
    content.widget.attrs.update({"placeholder": "Content"})

    class Meta:
        model = Question
        fields = ["title", "summary", "content", "difficulty", "approved", ]