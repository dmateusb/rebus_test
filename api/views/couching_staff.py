
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import *
from api.serializers import CouchingStaffSerializer
from django.shortcuts import get_object_or_404


class CouchingStaffListApiView(APIView):

    def get(self, request, *args, **kwargs):

        couching_staffs = CouchingStaff.objects.all()
        serializer = CouchingStaffSerializer(couching_staffs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        serializer = CouchingStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CouchingStaffDetailApiView(APIView):

    def get(self, request, couch_id, *args, **kwargs):

        todo_instance = get_object_or_404(CouchingStaff, id=couch_id)
        if not todo_instance:
            return Response(
                {"res": "Record with couch staff id doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CouchingStaffSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, couch_id=None):
		
        item = CouchingStaff.objects.get(id=couch_id)
        serializer = CouchingStaffSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, couch_id=None):

        item = get_object_or_404(CouchingStaff, id=couch_id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

