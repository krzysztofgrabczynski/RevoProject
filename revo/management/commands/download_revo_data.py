from django.core.management.base import BaseCommand
import requests
import json


class APIException(Exception):
    pass


class Command(BaseCommand):
    API_URL = "https://example.pl/api/download-revo-data"
    
    def handle(self, *args, **options):
        try:
            revo_data_response = self.fetch_revo_data()
            revo_json_data = revo_data_response.json()
            self.validate_data(revo_json_data)
                
        except json.JSONDecodeError:
            raise ValueError("Cannot parse data to json object")
        
        except (APIException, ValueError) as error:
            raise error

        for item in revo_json_data:
            self.stdout.write(json.dumps(item, indent=2)) 
    
    def fetch_revo_data(self) -> requests.Response:
        try:
            revo_data_response = requests.get(self.API_URL)
        except requests.ConnectionError as e:
            raise APIException("Connection error")

        if revo_data_response.status_code != 200:
            raise APIException("Error status code")
        
        return revo_data_response
    
    def validate_data(self, data: list) -> None:
        if not isinstance(data, list):
            raise ValueError("Data expected to be a list")
        
        for item in data:
            if not isinstance(item["id"], int):
                raise ValueError("Field 'id' must be an integer")
            if not isinstance(item["name"], str):
                raise ValueError("Field 'name' must be a string")
            if not isinstance(item["is_active"], bool):
                raise ValueError("Field 'is_active' must be a boolean")
            if not isinstance(item["tags"], list) or not all(isinstance(tag, str) for tag in item["tags"]):
                raise ValueError("Field 'tags' must be a list of strings")
            