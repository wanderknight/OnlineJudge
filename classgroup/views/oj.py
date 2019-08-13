__author__ = 'wanderknight'
__time__ = '2019/8/9 20:32'

from utils.api import APIView

from classgroup.models import Classgroup
from classgroup.serializers import ClassgroupSerializer


class ClassgroupAPI(APIView):
    def get(self, request):
        classgroups = Classgroup.objects.filter()
        return self.success(self.paginate_data(request, classgroups, ClassgroupSerializer))
