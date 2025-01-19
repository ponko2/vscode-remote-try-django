from datetime import date
from typing import Any, List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router, Schema

from employees.models import Employee

router = Router()


def to_lower_camel_case(string: str) -> str:
    first, *rest = string.split("_")
    return first.lower() + "".join(word.capitalize() for word in rest)


class BaseSchema(Schema):
    class Config(Schema.Config):
        alias_generator = to_lower_camel_case
        populate_by_name = True


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


@router.get("", response=List[EmployeeOut], by_alias=True)
def list(request: HttpRequest) -> Any:
    return Employee.objects.all()


@router.post("")
def create(request: HttpRequest, payload: EmployeeIn) -> dict[str, int]:
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}


@router.get("/{employee_id}", response=EmployeeOut, by_alias=True)
def retrieve(request: HttpRequest, employee_id: int) -> Any:
    return get_object_or_404(Employee, id=employee_id)


@router.put("/{employee_id}")
def update(
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
def destroy(request: HttpRequest, employee_id: int) -> dict[str, bool]:
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return {"success": True}
