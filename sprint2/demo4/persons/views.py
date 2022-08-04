import ipdb
from django.forms.models import model_to_dict
from rest_framework.views import APIView, Response, status

from persons.models import Person


class PersonView(APIView):
    # sobrescrita
    def get(self, request):
        # return Response({"data": "hello get"})
        # SELECT * FROM persons_person;
        persons = Person.objects.all()

        # return Response(persons)
        # persons_list = []

        # for person in persons:
        #     person_dict = model_to_dict(person)
        #     persons_list.append(person_dict)

        persons_list = [model_to_dict(person) for person in persons]

        return Response(persons_list)

    def post(self, request):
        # return Response({"data": "hello post"})
        # ipdb.set_trace()
        # person = Person.objects.create(name=request.data["name"])
        # person = Person.objects.create(name=request.data.get("name"))
        person = Person.objects.create(**request.data)

        person_dict = model_to_dict(person)

        # return Response(person_dict, 201)
        return Response(person_dict, status.HTTP_201_CREATED)


class PersonDetailView(APIView):
    # SELECT * FROM persons_person WHERE id=1
    # SELECT * FROM persons_person WHERE id='1'

    def get(self, request, person_id: int):
        # SELECT * FROM persons_person WHERE id=1
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"details": "person not found"}, status.HTTP_404_NOT_FOUND)

        person_dict = model_to_dict(person)

        return Response(person_dict)

    def patch(self, request, person_id: int):
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"details": "person not found"}, status.HTTP_404_NOT_FOUND)

        # ipdb.set_trace()
        # person.name = request.data.get("name", person.name)
        # person.cpf = request.data.get("cpf", person.cpf)
        # person.email = request.data.get("email", person.email)
        # person.birthdate = request.data.get("birthdate", person.birthdate)
        # person.married = request.data.get("married", person.married)
        # person.account_balance = request.data.get(
        #     "account_balance", person.account_balance
        # )

        for key, value in request.data.items():
            setattr(person, key, value)

        person.save()

        person_dict = model_to_dict(person)

        return Response(person_dict, status.HTTP_200_OK)

    def delete(self, request, person_id: int):
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"details": "person not found"}, status.HTTP_404_NOT_FOUND)

        person.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonSearchView(APIView):
    def get(self, request):
        # ipdb.set_trace()

        account_balance_param = request.query_params.get("account_balance_gt")
        name_param = request.query_params.get("name")

        # WHERE ... AND ... ILIKE %alex%
        persons = Person.objects.filter(
            account_balance__gt=account_balance_param, name__contains=name_param
        )

        filtered_persons = [model_to_dict(person) for person in persons]

        return Response(filtered_persons, status.HTTP_200_OK)
