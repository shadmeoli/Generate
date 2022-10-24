from BASE import *


# system configuration and details
class ComputerDetails:

    def __init__(self):

        self.computer_essentials = {}

        # cheaking for essentials details fro the computer from where the app was generated at
        # creating the file in the current directory
        self.environ = os.environ

        # writing to the computer_essentials dictionary
        # getting the os details and path
        self.computer_essentials["user_name"] = self.environ['USERNAME']
        self.computer_essentials["computer_name"] = self.environ['COMPUTERNAME']
        self.computer_essentials["home_path"] = self.environ['HOMEPATH']
        self.computer_essentials["os_type"] = self.environ['OS']

    # writing to the computer_essentials dictionary
    def essentials(self) -> dict:
        return json.dumps(self.computer_essentials, indent=4)


# mew image input vaidation
@dataclass
class ImageConfiguration:

    # these will be the default values if you decide to use the defult configuration
    image_name: Optional[str] = "new_image"
    postgres_user: Optional[str] = "postgres"
    postgres_password: Optional[str] = "password"
    db_name: Optional[str] = "postgres"
    port: Optional[str] = 5432
    volums: Optional[str] = "./db-data/:/var/lib/postgresql/data/"


@dataclass
class LevelAddidition:

    db_name: str
    db_version: str
    db_type: str


# to env configs
@dataclass
class EnvConfigs:

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

# database CRUD operations
# writing to database for subscriber to keep
# tack of the number of times the have create an app
@lru_cache
class DatabaseOperations:

    def __init__(self, ):

        self.new_config_file = None
        self.file = "docker-compose.yaml"

    # creating a configuration file wi'response.csv'th a list of created apps and other details related with the app
    def create_configuration_file(self, **kwargs: ImageConfiguration) -> bool:

        try:
            with open(self.file, 'w+') as data_file:
                new_file = yaml.dump(kwargs, data_file)
                return True
        except:
            # creating the file form the terminal
            self.new_config_file = os.system(f'touch {self.file}')
            return True

    # reading the file directly
    def directRead(self, _file): # takes in a path as an argument
        # exclusive var
        details = open(_file, 'w')
        return details

    # reading values from the config file

    def redingDetailsFromDatabase(self) -> dict:  # return

        # creating 'response.csv the file in directory
        try:
            with open(self.file, '+r') as config_file:
                config_data_file = yaml.load(config_file, Loader=Loader)
                return config_data_file

        except TypeError as e:
            return e

    # [TODO] -> Make function Async and pass db configs as  args
    # inserting values in the db
    def addDetailsToConfigFile(self, **kwargs: LevelAddidition):  # takes in key arguments of the configs to add to the new docker file
        # empty dic to store values fot svaing in the config file
        self.app_configuration = {}
        self.serilized_app_configuration = {}
        self.upper_level = {}

        # [TODO] ->  Add database configuration (postgres)
        # key  values
        self.app_configuration['db_version'] = app_version # this is docker's image version
        self.app_configuration['db_name'] = db_name
        self.app_configuration['db_type'] = app_type

        # serilizing the dict
        self.serilized_app_configuration[app_name] = self.app_configuration
        self.upper_level['elixer_db'] = self.serilized_app_configuration

        # creating request trials in case of file change
        try:
            # writing to the config file
            configuration_file = self.directRead(self.file)
            configuration = yaml.dump(
                self.upper_level, configuration_file, indent=4)

            return self.upper_level

        # raising the exception error
        except TypeError as e:
            raise e
        # return a false response for other errors
        except:
            return False



'''
    Runnig the operations to execute docker
'''


class Composer:

    