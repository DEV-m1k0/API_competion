from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .logic.hospital import (get_all, get_rooms, get_info_by_id,
                             hospital_create, update_hospital_by_id,
                             delete_hospital_by_id)
from .models import Hospital
from rest_framework import status

# Create your views here.


class HospitalsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request: Request, id: int = False):

        if id:
            response = get_info_by_id(request=request, id=id)
            return response
        
        else:
            response = get_all(request=request)
            return response
        
    def put(self, request: Request, id: int):

        response = update_hospital_by_id(request=request, id=id)

        return response

    def post(self, request: Request):

        response = hospital_create(request=request)

        return response

    def delete(self, request: Request, id: int):

        response = delete_hospital_by_id(request=request, id=id)

        return response


class RoomsByIdAPIView(APIView):
    def get(self, request: Request, id: int):
        hospital = Hospital.objects.get(pk=id)
        rooms = get_rooms(hospital=hospital)

        return Response({
            "rooms": rooms
        }, status=status.HTTP_200_OK)
    
