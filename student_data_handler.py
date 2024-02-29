import requests
import redis
import json
import yaml

class StudentDataHandler:
    """
    A class to handle the retrieval and storage of student data using Redis.
    """
    
    def __init__(self, config_path):
        """
        Initializes the connection to Redis using the provided configuration.
        
        :param config_path: Path to the YAML configuration file.
        """
        self.config = self.load_config(config_path)
        redis_config = self.config['redis']
        self.r = redis.Redis(
            host=redis_config.get('host', 'localhost'),
            port=redis_config.get('port', 6379),
            db=redis_config.get('db', 0),
            username=redis_config.get('user', None),
            password=redis_config.get('password', None),
            decode_responses=True
        )
        self.redis_key = 'students'
        self._students = None  # Internal attribute to cache the students data

    def load_config(self, path):
        """
        Loads the YAML configuration from the specified path.

        :param path: Path to the YAML file.
        :return: Loaded configuration as a dictionary.
        """
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    def fetch_students_from_api(self):
        """
        Fetches student data from a JSON API based on the URL in the config file.
        """
        api_url = self.config.get('api_url', "http://localhost:3000/students")
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from the server. Status code: {response.status_code}")
            return None

    def load_student_data(self):
        """
        Loads student data from Redis, fetching from the API if necessary.
        This method populates the internal _students attribute.
        """
        students_data = self.r.get(self.redis_key)

        if students_data:
            self._students = json.loads(students_data)
            print("Loaded students data from Redis.")
        else:
            self._students = self.fetch_students_from_api()
            if self._students:
                self.r.set(self.redis_key, json.dumps(self._students))
                print("Fetched students data from JSON server and stored in Redis.")

    def get_students(self, limit=None):
        """
        Getter method to retrieve student data.

        :param limit: The maximum number of student records to return. If None, all records are returned.
        :return: A list of student data dictionaries, limited by the specified amount.
        """
        # Load data if it hasn't been loaded yet
        if self._students is None:
            self.load_student_data()

        # Return the data, applying the limit if specified
        return self._students[:limit] if limit is not None else self._students
