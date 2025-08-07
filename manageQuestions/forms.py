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
    title.widget.attrs.update({"placeholder": "Title (Max 100 Characters)",
                               "class": "question-edit-title"})
    summary.widget.attrs.update({"placeholder": "Summary (Max 200 Characters)",
                                 "class": "question-edit-summary"})
    content.widget.attrs.update({"placeholder": "Content",
                                 "class": "question-edit-content"})
    difficulty.widget.attrs.update({"class": "question-edit-difficulty"})
    approved.widget.attrs.update({"class": "question-edit-summary"})

    class Meta:
        model = Question
        fields = ["title", "summary", "content", "difficulty", "approved", ]


class QuestionEditForm(forms.ModelForm):
    """
    form for editing a question
    """
    title = forms.CharField(label="Title", max_length=100)
    summary = forms.CharField(label="Summary", max_length=200)
    content = forms.CharField(label="Content", widget=forms.Textarea)
    difficulty = forms.ChoiceField(choices=DIFFICULTY, label="Difficulty")
    approved = forms.ChoiceField(choices=STATUS, label="Save or Submit?")

    # add classes for styling
    title.widget.attrs.update({"placeholder": "Title (Max 100 Characters)",
                               "class": "question-edit-title",
                               "id": "id_title_edit"})
    summary.widget.attrs.update({"placeholder": "Summary (Max 200 Characters)",
                                 "class": "question-edit-summary",
                                "id": "id_summary_edit"})
    content.widget.attrs.update({"placeholder": "Content",
                                 "class": "question-edit-content",
                                "id": "id_content_edit"})
    difficulty.widget.attrs.update({"class": "question-edit-difficulty",
                                    "id": "id_difficulty_edit"})
    approved.widget.attrs.update({"class": "question-edit-summary",
                                  "id": "id_approved_edit"})

    class Meta:
        model = Question
        fields = ["title", "summary", "content", "difficulty", "approved", ]
