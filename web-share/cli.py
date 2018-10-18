import click
import os
import subprocess as sp

import share

@click.command()
@click.argument('arg')
def main(arg):
	"""This serves your local files to your local Network
	   Author: Ove Bepari

	"""
	if arg == 'serve':
		os.environ['FLASK_APP'] = 'share.py'
		sp.call(['flask run --host=0.0.0.0'], shell=True)

	else:
		print("Something went wrong.")
		print("or You're on a Windows machine")


if __name__ == '__main__':
	main()