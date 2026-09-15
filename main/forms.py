from django.forms import ModelForm
from main.models import Education

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