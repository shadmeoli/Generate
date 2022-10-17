# from rich.prompt import Prompt

from BASE import *


from operations import ImageConfiguration, LevelAddidition, EnvConfigs

# CLI config
app = typer.Typer()
hes_running = emoji.emojize(":person_running:")

# [TODO] -> call other function on the entry
# the function to run when executing the cli


# emojis
indicator = {
	"doing" : emoji.emojize(":small_red_triangle_down:"),
	"error" : emoji.emojize(":bangbang:"),
	"pending" : emoji.emojize(":clock930:"),
	"success" : emoji.emojize(":tada:"),
	"done" : emoji.emojize(":ballot_box_with_check:")
}


def gen(*args):
	print("Shad")


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
def gen(
	image_name = Prompt.ask(f"[green bold] {indicator['doing']} Image name :", default="new_image"),
	postgres_user= Prompt.ask(f"[green bold] {indicator['doing']} postgres username :", default="postgres"),
	db_name = Prompt.ask(f"[green bold] {indicator['doing']}  Database name:", default="postgres"),
	port: int = Confirm.ask(f"[green bold] {indicator['doing']} Use default psql port", default="5432"),
	volumes = Confirm.ask(f"[green bold] {indicator['doing']}  Use default volume", default="./db-data/:/var/lib/postgresql/data/")
	):

	
	""" [TODO] ->  Default values read and validation form the operations file
				-> create a yaml config file from the user input file
				-> store configs in a seperate yaml config and 
					monitor the changes with watch dogs for any new configs and appy the changes on user's request 
	""" 


if __name__ == '__main__':
	app()
