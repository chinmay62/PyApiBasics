import requests


class api_operations:
    def api_get(self, endpoint: str, headers: dict, params: dict, body: dict):
        response = None
        try:
            options = {}
            if headers is not None:
                options["headers"] = headers

            if params is not None:
                options["params"] = params

            if body is not None:
                options["json"] = body

            response = requests.get(url=endpoint, **options)
        except Exception as e:
            print(f"An error occurred: {e}")
            response = None
        finally:
            return response
