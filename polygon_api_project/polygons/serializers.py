from rest_framework import serializers
from .models import PolygonRegion
import json

class PolygonRegionSerializer(serializers.ModelSerializer):
    points = serializers.ListField(
        child=serializers.ListField(child=serializers.FloatField()),
        help_text="List of [x, y] points"
    )

    class Meta:
        model = PolygonRegion
        fields = ['id', 'name', 'points']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['points'] = json.loads(instance.points)
        return ret

    def to_internal_value(self, data):
        internal = super().to_internal_value(data)
        internal['points'] = json.dumps(internal['points'])
        return internal
