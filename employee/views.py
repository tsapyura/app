from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from employee.models import Employee
from employee.permissions import IsLoggedInUserOrAdmin
from employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == "create":
            permission_classes = [AllowAny]
        elif (
            self.action == "retrieve"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == "list" or self.action == "destroy":
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
