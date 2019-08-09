__author__ = 'wanderknight'
__time__ = '2019/8/9 20:33'
from utils.api import serializers
from utils.api._serializers import UsernameSerializer
from .models import Classgroup


class ClassgroupSerializer(serializers.ModelSerializer):
    created_by = UsernameSerializer()

    class Meta:
        model = Classgroup
        fields = "__all__"
