from rest_framework import serializers
from base_app.models import *

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

def validate_date_range(date_range):
    start_date = date_range.get('start')
    end_date = date_range.get('end')

    if start_date and end_date and start_date > end_date:
        raise serializers.ValidationError("Start date cannot be after end date.")

class OrderReportRequestSerializer(serializers.Serializer):
    skus = serializers.ListField(required=False)
    date_range = serializers.DictField(
        child=serializers.DateField(format="%Y-%m-%d"),
        required=False,
        validators=[validate_date_range],
    )