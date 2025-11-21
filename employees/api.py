from datetime import date

from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from pydantic import ConfigDict

from employees.models import Employee

router = Router()


def to_lower_camel_case(string: str) -> str:
    first, *rest = string.split("_")
    return first.lower() + "".join(word.capitalize() for word in rest)


class BaseSchema(Schema):
    model_config = ConfigDict(
        alias_generator=to_lower_camel_case,
        populate_by_name=True,
    )


class EmployeeIn(BaseSchema):
    first_name: str
    last_name: str
    department_id: int | None = None
    birthdate: date | None = None


class EmployeeOut(BaseSchema):
    id: int
    first_name: str
    last_name: str
    department_id: int | None = None
    birthdate: date | None = None


@router.get("", response=list[EmployeeOut], by_alias=True)
def list_employees(request: HttpRequest) -> QuerySet[Employee]:
    return Employee.objects.all()


@router.post("")
def create_employee(request: HttpRequest, payload: EmployeeIn) -> dict[str, int]:
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}


@router.get("/{employee_id}", response=EmployeeOut, by_alias=True)
def get_employee(request: HttpRequest, employee_id: int) -> Employee:
    return get_object_or_404(Employee, id=employee_id)


@router.put("/{employee_id}")
def update_employee(
    request: HttpRequest,
    employee_id: int,
    payload: EmployeeIn,
) -> dict[str, bool]:
    employee = get_object_or_404(Employee, id=employee_id)
    for attr, value in payload.dict().items():
        setattr(employee, attr, value)
    employee.save()
    return {"success": True}


@router.delete("/{employee_id}")
def delete_employee(request: HttpRequest, employee_id: int) -> dict[str, bool]:
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return {"success": True}
