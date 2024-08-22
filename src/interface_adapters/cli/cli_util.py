def is_success(response: dict) -> bool:
    return response['statusCode'] == 'success'
