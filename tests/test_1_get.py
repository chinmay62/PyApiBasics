import pytest
from libs import config_ops
from libs import api_ops
from config.constants import api_response_codes


class Test_Get:
    config = config_ops.config_operations()
    api = api_ops.api_operations()

    @pytest.mark.order(101)
    @pytest.mark.get
    def test_get_001(self):
        _endpoint = self.config.get_base_url()
        _response = self.api.api_get(
            endpoint=_endpoint, headers=None, params=None, body=None
        )
        assert (
            _response.status_code == api_response_codes.OK
        ), f"Invalid response code.  Expecting 200, received {_response.status_code}."
