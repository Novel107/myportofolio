from django.utils.html import strip_tags
from rest_framework import serializers
from main.models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category", "category_display", 
            "is_ongoing", "star_count", "is_starred", "starred_by_names"
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Judul pengalaman tidak boleh kosong.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return obj.starred_by.filter(pk=request.user.pk).exists()

    def get_starred_by_names(self, obj):
        names = list(obj.starred_by.values_list("username", flat=True)[:3])
        if obj.starred_by.count() > 3:
            names.append("...")
        return ", ".join(names)