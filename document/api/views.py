from rest_framework.views import APIView
from .logic import history
from .permissions import AdminOrManagerOrDoctorPermission, DoctorOrPacientPermission

# Create your views here.

class HistoryAPIView(APIView):
    # permission_classes = [AdminOrManagerOrDoctorPermission]
    
    def get(self, request, id):
        response = history.get_history(id)
        return response
    
    def post(self, request):
        response = history.post_history(request)
        return response
    
    def put(self, request, id):
        response = history.put_history(request, id)
        return response
    

class HistoryPacientAPIView(APIView):
    permission_classes = [DoctorOrPacientPermission]
    def get(self, request, id):
        response = history.get_history_by_pacient(id)
        return response