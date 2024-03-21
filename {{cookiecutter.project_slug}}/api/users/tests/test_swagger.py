from http import HTTPStatus

from django.urls import reverse


def test_swagger_accessible_by_admin(admin_client):
    url = reverse("api-docs")
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_api_schema_generated_successfully(admin_client):
    url = reverse("schema")
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK
