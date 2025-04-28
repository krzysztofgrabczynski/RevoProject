import io, json
from django.test import TestCase
from django.core.management import call_command
from rest_framework.exceptions import APIException
from unittest.mock import patch
from requests.exceptions import ConnectionError

# from revo.management.commands.download_revo_data import APIException


class DownloadRevoDataCommandTests(TestCase):
    @patch("revo.management.commands.download_revo_data.requests.get")
    def test_connection_error(self, mock_get):
        mock_get.side_effect = ConnectionError()

        with self.assertRaises(APIException) as e:
            call_command("download_revo_data")
        
        self.assertEqual("Connection error", str(e.exception))

    @patch("revo.management.commands.download_revo_data.requests.get")
    def test_non_200_status_code(self, mock_get):
        mock_get.return_value.status_code = 400

        with self.assertRaises(APIException) as e:
            call_command("download_revo_data")
        
        self.assertEqual("Error status code", str(e.exception))

    @patch("revo.management.commands.download_revo_data.requests.get")
    def test_invalid_data_format(self, mock_get):
        mock_get.return_value.status_code = 200
        invalid_json_data = {"invalid_field": "invalid_value"}
        mock_get.return_value.json.return_value = invalid_json_data

        with self.assertRaises(ValueError) as e:
            call_command("download_revo_data")
        
        self.assertEqual("Data expected to be a list", str(e.exception))

    @patch("revo.management.commands.download_revo_data.requests.get")
    def test_successful_data_fetch(self, mock_get):
        mock_get.return_value.status_code = 200
        valid_json_data = [
            {
                "id": 1,
                "name": "Test Name 1",
                "is_active": True,
                "tags": ["revo", "test"]
            },
            {
                "id": 2,
                "name": "Test Name 2",
                "is_active": False,
                "tags": []
            }
        ]
        mock_get.return_value.json.return_value = valid_json_data
        out = io.StringIO()

        call_command("download_revo_data", stdout=out)
        output = out.getvalue()
    
        expected_output = "\n".join([json.dumps(item, indent=2) for item in valid_json_data]) + "\n"
        self.assertEqual(output, expected_output)
