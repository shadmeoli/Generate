# from rich.prompt import Prompt

from BASE import *

from operations import *
from operations import ImageConfiguration, LevelAddidition, EnvConfigs
from operations import DatabaseOperations

# CLI config
app = typer.Typer()
hes_running = emoji.emojize(":person_running:")

# [TODO] -> call other function on the entry
# the function to run when executing the cli


# emojis
indicator = {
    "doing": emoji.emojize(":small_red_triangle_down:"),
    "error": emoji.emojize(":bangbang:"),
    "pending": emoji.emojize(":clock930:"),
    "success": emoji.emojize(":tada:"),
    "done": emoji.emojize(":ballot_box_with_check:")
}

# command to create a new image with specified configiration
"""
These are the key word agruments to pass:

	image_name = "new_image"
	postgres_user = "postgres"
	postgres_password = "password"
	db_name = "postgres"
	port= 5432
	volums = "./db-data/:/var/lib/postgresql/data/
"""


@app.command()
def new():

    # asking for user configuration
    image_name = Prompt.ask(f"[green bold] {indicator['doing']} Image name :", default="new_image")
    postgres_user = Prompt.ask(f"[green bold] {indicator['doing']} postgres username :", default="postgres")
    db_name = Prompt.ask(f"[green bold] {indicator['doing']}  Database name:", default="postgres")
    volumes = Confirm.ask(f"[green bold] {indicator['doing']}  Use default volume", default="./db-data/:/var/lib/postgresql/data/")

    """
		[TODO] 	-> parse inputs to the operations modules
				-> validate the data inputs and generate a table in report
				-> start a docker image 
	"""

    # the file configurations for the yaml file as per docker image
    file_default_configuration = {
        "version": 2.3,
        "services": [{
            image_name: [{
                "image: postgres": 12,
                "mem_limit": "1536MB",
                "mem_reservation": "1G",
                "environment": [{
                    "POSTGRES_USER": postgres_user,
                    "POSTGRES_PASSWORD": "a1128f69-e6f7-4e93-a2df-3d4db6030abc"
                }],
                "ports": ["5442:5432"],
                "networks": ["image_name_network"],
                "volumes": [volumes]
            }],
        }],

        "networks": [{
            "image_name_network": [{
                "driver": "bridge"
            }],
        }],

        "volumes": [{
            "db-data": db_name
        }]
    }

    # with open('config.json', 'w') as json_file:
    # json.dump(configuration, json_file)
    cons = Console()
    cons.print(file_default_configuration)

    config = DatabaseOperations()

    # db_name = 'postgres'
    # image_name = 'new_image'
    # port = '5432'
    # postgres_user = 'postgres'
    # volumes = './db-data/:/var/lib/postgresql/data/'

    config_details = config.create_configuration_file(
    	db_name=db_name,
    	image_name=image_name,
    	postgres_user=postgres_user,
    	volumes=volumes
    	)

    if config_details:
    	with open("docker-compose.yaml", 'w+') as data_file:
            new_file = yaml.dump(file_default_configuration, data_file)
    else:
    	cons.error("Error processing the crud operation")


@app.command()
def check():
    print("The config file")


if __name__ == '__main__':
    app()
