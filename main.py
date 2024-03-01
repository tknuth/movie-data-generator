import sys

import click
import pandas as pd
from loguru import logger

from movie_data_generator import Simulation

CUSTOM_FORMAT = "<fg #888>{time:YYYY-MM-DD HH:mm:ss}</fg #888> {level} {message}"
logger.configure(handlers=[{"sink": sys.stderr, "format": CUSTOM_FORMAT}])


@click.command()
@click.argument("path", type=click.Path())
def cli(path):
    simulation = Simulation()
    simulation.run()
    pd.DataFrame(
        {"signup_date": [user.signup_date for user in simulation.environment.users]}
    ).to_json(path, orient="records", index=False, indent=4)


if __name__ == "__main__":
    cli()
