import requests
import pytest
import setup

error_messages = {
    'Alcohol_E_024': 'err_id_required: Alcohol_E_024  ',
    'Alcohol_E_025': 'err_id_number: Alcohol_E_025 ',
    'Alcohol_E_026': 'err_id_not_exist: Alcohol_E_026  ',
}


@pytest.mark.parametrize('id_field', [1000, 'a', 78, ''])
def test_delete(id_field):
    response = requests.post(f"{setup.base_url}/api/v1/alcohol/test/delete?id={id_field}", headers=setup.headers)
    setup.process_response(response, error_messages)
