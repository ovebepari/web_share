import click
import os
import subprocess as sp

from web_share_ftp import share

app_location = share.__file__

@click.command()
@click.argument('arg')
def main(arg):
	"""This serves your local files to your local Network
	   Author: Ove Bepari

	"""
	if not arg:
		print("You did't provide any argument. Run with --help argument")
	if arg == 'serve':
		os.environ['FLASK_APP'] = app_location
		sp.call(['flask run --host=0.0.0.0'], shell=True)

	else:
		print("Something went wrong.")
		print("or You're on a Windows machine")


if __name__ == '__main__':
	main()