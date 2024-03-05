import random
from typing import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from loguru import logger

from .user import User
from .environment import Environment


@dataclass(frozen=True)
class Config:
    signup_probability: float = 0.1
    step_size: Callable = lambda: timedelta(days=random.randint(4, 14))
    watch_probability: Callable = lambda: random.uniform(0, 1)


@dataclass
class Simulation:
    config: Config = field(default_factory=Config)
    env: Environment = field(default_factory=Environment)

    def run(self):
        while self.env.date < datetime.now():
            self.make_turn()

    def make_turn(self):
        # register new user
        if random.random() < self.config.signup_probability:
            user = spawn_user(self.config, self.env)
            self.env.users.append(user)
            logger.info(f"{user.signup_date}: New user signed up.")

        # watch movies
        for user in self.env.users:
            user.make_turn(self.env)

        # increment time
        self.env.date += Config.step_size()


def spawn_user(config: Config, env: Environment):
    return User(
        age=random.randint(18, 65),
        signup_date=env.date + timedelta(minutes=random.randint(0, 24 * 60)),
        watch_probability=config.watch_probability(),
        profile=random.choice(env.profiles),
    )
