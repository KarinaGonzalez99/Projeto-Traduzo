from src.models.history_model import HistoryModel
import json


# Req. 7
def test_request_history(prepare_base):
    expected_data = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]

    response_json = HistoryModel.list_as_json()

    response_data = json.loads(response_json)

    for item in response_data:
        item.pop("_id")

    assert response_data == expected_data
