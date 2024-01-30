import requests
import pytest
import setup

error_messages = {
    'ListAlcoholTest_001_E_003': 'err_limit_required: ListAlcoholTest_001_E_003 ',
    'ListAlcoholTest_001_E_004': 'err_limit_number: ListAlcoholTest_001_E_004 ',
    'ListAlcoholTest_001_E_005': 'err_limit_min: ListAlcoholTest_001_E_005 ',
    'ListAlcoholTest_001_E_006': 'err_offset_required: ListAlcoholTest_001_E_006  ',
    'ListAlcoholTest_001_E_007': 'err_offset_number: ListAlcoholTest_001_E_007  ',
    'ListAlcoholTest_001_E_008': 'err_offset_min: ListAlcoholTest_001_E_008 ',
}


@pytest.mark.parametrize('limit', [10, 'a', 0, ''])
def test_limit(limit):
    response = requests.get(f"{setup.base_url}/api/v1/alcohol/test/list?limit={limit}&offset=0", headers=setup.headers)
    setup.process_response(response, error_messages)


@pytest.mark.parametrize('offset', [-1, 'a', 0, ''])
def test_offset(offset):
    response = requests.get(f"{setup.base_url}/api/v1/alcohol/test/list?limit=10&offset={offset}",
                            headers=setup.headers)
    setup.process_response(response, error_messages)
