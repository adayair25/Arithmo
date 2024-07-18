import os


class Validation:

    def __init__(self, directory_path):
        self.directory_path = directory_path

    def read_files(self):  # Verification that the directory exists
        if not os.path.isdir(self.directory_path):
            raise Exception('Error: directory does not exist')
        content = []
        for filename in os.listdir(self.directory_path):  # File extension verification
            if filename.endswith('.ar'):
                file_path = os.path.join(self.directory_path, filename)
                with open(file_path, 'r') as file:  # File reading
                    content = file.read().replace('\n', '')
        return content
