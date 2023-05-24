import json
import logging

class DataStorage:
    @staticmethod
    def store_data(data, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            logging.getLogger('DataStorage').info(f"Successfully stored data in {filename}.")
        except Exception as e:
            logging.getLogger('DataStorage').error(f"An error occurred while storing data in {filename}.")
            raise e
