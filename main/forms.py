from django.forms import ModelForm
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
            "company", 
            "start_year", 
            "end_year", 
            "description",
        ]