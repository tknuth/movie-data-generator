import sys

import click
from pathlib import Path
import pandas as pd
import json
from loguru import logger
from dataclasses import asdict

from movie_data_generator import Simulation

CUSTOM_FORMAT = "<fg #888>{time:YYYY-MM-DD HH:mm:ss}</fg #888> {level} {message}"
logger.configure(handlers=[{"sink": sys.stderr, "format": CUSTOM_FORMAT}])


@click.command()
@click.argument("path", type=click.Path())
def cli(path):
    sim = Simulation()
    sim.run()
    json.dump([m.to_dict() for m in sim.env.movies], Path(path).open("w"), indent=4)
    # pd.DataFrame(
    #     {"signup_date": [user.signup_date for user in sim.env.users]}
    # ).to_json(path, orient="records", index=False, indent=4)


if __name__ == "__main__":
    cli()
