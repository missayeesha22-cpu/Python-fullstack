from rest_framework import serializers
from .models import student_table

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = student_table
        fields = '__all__'

    def validate_reg_no(self, value):
        if student_table.objects.filter(reg_no=value).exists():
            raise serializers.ValidationError(
                "This registration number already exists."
            )
        return value