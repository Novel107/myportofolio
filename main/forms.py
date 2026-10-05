from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Education, Experience

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution_name",
            "degree",
            "major",
            "start_year",
            "end_year",
            "description",
        ]

#Form Experience
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title", 
            "category", 
            "description", 
            "thumbnail",
            "ended_at"
        ]

def clean_title(self):
        title = self.cleaned_data.get('title', '')
        return strip_tags(title)

def clean_description(self):
        description = self.cleaned_data.get('description', '')
        return strip_tags(description)