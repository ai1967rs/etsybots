import json
import logging

class DataExporter:
    def __init__(self):
        self.logger = logging.getLogger('DataExporter')

    def export_data(self, data, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            self.logger.info(f"Successfully exported data to {filename}.")
        except Exception as e:
            self.logger.error(f"An error occurred while exporting data to {filename}: {e}")
            raise e
