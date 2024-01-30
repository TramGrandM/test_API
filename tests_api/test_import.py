import requests
import pytest
import setup

error_messages = {
    '["Alcohol_E_017","Alcohol_E_023","Alcohol_E_021"]': 'err_required: Alcohol_E_017, Alcohol_E_023, Alcohol_E_021 ',
    'Alcohol_E_017': 'err_value_required: Alcohol_E_017',
    'Alcohol_E_018': 'err_value_number: Alcohol_E_018',
    'Alcohol_E_019': 'err_value_min: Alcohol_E_019 ',
    'Alcohol_E_020': 'err_value_max: Alcohol_E_020 ',
    'Alcohol_E_021': 'err_mac_address_required: Alcohol_E_021  ',
    'Alcohol_E_022': 'err_mac_address_wrong_format: Alcohol_E_022 ',
    'Alcohol_E_023': 'err_device_name_required: Alcohol_E_023 ',
}


@pytest.mark.parametrize("data", [
    {"value": 0.88, "mac_address": "00:00:00:00:00:00", "device_name": "IRISALC_111"},
    {"value": 'aaa', "mac_address": "00:00:00:00:00:00", "device_name": "IRISALC_111"},
    {"value": -8, "mac_address": "00:00:00:00:00:00", "device_name": "IRISALC_111"},
    {"value": "", "mac_address": "00:00:00:00:00:00", "device_name": "IRISALC_111"},
])
def test_value(data):
    response = requests.post(f"{setup.base_url}/api/v1/alcohol/test/import", headers=setup.headers, json=data)
    setup.process_response(response, error_messages)


@pytest.mark.parametrize("data_mac_address", [
    {"value": 0.8, "mac_address": "", "device_name": "IRISALC_111"},
    {"value": 0.8, "mac_address": "aaaa", "device_name": "IRISALC_111"},
])
def test_mac_address(data_mac_address):
    response = requests.post(f"{setup.base_url}/api/v1/alcohol/test/import", headers=setup.headers,
                             json=data_mac_address)
    setup.process_response(response, error_messages)


@pytest.mark.parametrize("data_device_name", [
    {"value": 0.8, "mac_address": "00:00:00:00:00:00", "device_name": ""},
])
def test_device_name(data_device_name):
    response = requests.post(f"{setup.base_url}/api/v1/alcohol/test/import", headers=setup.headers,
                             json=data_device_name)
    setup.process_response(response, error_messages)


@pytest.mark.parametrize("list_para", [
    {"value": 0.3, "mac_address": "00:00:00:00:00:00", "device_name": "IRISALC_111"},  # case input valid all fields
    {"value": "", "mac_address": "", "device_name": ""},  # case null
])
def test_list(list_para):
    response = requests.post(f"{setup.base_url}/api/v1/alcohol/test/import", headers=setup.headers,
                             json=list_para)
    setup.process_response(response, error_messages)
