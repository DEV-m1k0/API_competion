from django.http.request import HttpRequest
from rest_framework.response import Response
from api.models import Hospital, TimeTable, Room
from rest_framework import status
from .date import time_to_iso8601


def delete(request: HttpRequest, id: int):
    try:
        hospital = Hospital.objects.get(pk=id)
        hospital.timetables.all().delete()

        return Response({
            f"{hospital.name}": "Расписание удалено успешно!"
        }, status=status.HTTP_200_OK)
    
    except:
        return Response({
            "SERVER_ERROR": "Больница не найдена!"
        }, status=status.HTTP_404_NOT_FOUND)
    

def get_timetable(request: HttpRequest, id: int):
    try:
        hospital = Hospital.objects.get(pk=id)
        list_dates = time_to_iso8601(hospital.timetables.all())

        response = {}

        for id_date in range(1, len(list_dates)+1):
            time_table = list_dates[id_date-1]
            response[id_date] = {
                                "from": f"{time_table[0]}",
                                "to": f"{time_table[1]}"
                                }

        return Response({
            f"{hospital.name}": response
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"status": f"{e}"})
    

def get_timetable_by_room(request: HttpRequest, id: int, room: str):
    try:
        response = {}

        get_room = Room.objects.get(room=room)
        hospital = Hospital.objects.get(rooms=get_room)
        list_dates = time_to_iso8601(hospital.timetables.all())

        for id_date in range(1, len(list_dates)+1):
            time_table = list_dates[id_date-1]
            response[get_room.room] = {f'{id_date}': {
                                "from": f"{time_table[0]}",
                                "to": f"{time_table[1]}"
                                }}

        return Response({
            f"{hospital.name}": response
        }, status=status.HTTP_200_OK)
    
    except:
        return Response({
            "SERVER_ERROR": "Больница или комната не найдены!"
        }, status=status.HTTP_404_NOT_FOUND)