import sys

import click
from pathlib import Path
import pandas as pd
import json
from loguru import logger
from movie_data_generator.environment import Table
from dataclasses import asdict
from data_signals.variables import NumericVariable
from movie_data_generator import Simulation

CUSTOM_FORMAT = "<fg #888>{time:YYYY-MM-DD HH:mm:ss}</fg #888> {level} {message}"
logger.configure(handlers=[{"sink": sys.stderr, "format": CUSTOM_FORMAT}])


@click.command()
@click.argument("path", type=click.Path())
def cli(path):
    sim = Simulation()
    sim.run()

    d = {}

    for movie in sim.env.movies:
        d[movie.slug] = movie.to_dict()

    df = Table.from_ratings(sim.env.ratings)

    for slug, group in df.groupby("slug"):
        d[slug]["stats"] = (
            NumericVariable(group.score).histogram(range=[0, 1]).evaluate()
        )

    with (Path(path) / "movies.json").open("w") as file:
        json.dump([movie for movie in d.values()], file, indent=4)

    # pd.DataFrame(
    #     {"signup_date": [user.signup_date for user in sim.env.users]}
    # ).to_json(path, orient="records", index=False, indent=4)


if __name__ == "__main__":
    cli()
