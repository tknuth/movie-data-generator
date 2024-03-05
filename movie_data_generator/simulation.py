import random
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from loguru import logger

from .user import User
from .profile import Profile, load_profiles


@dataclass
class Environment:
    users: list[User] = field(default_factory=list)
    date: int = datetime(1990, 1, 1)
    profiles: list[Profile] = field(default_factory=load_profiles)


@dataclass(frozen=True)
class Config:
    signups: tuple[int, int] = (0, 10)


@dataclass
class Simulation:
    config: Config = field(default_factory=Config)
    environment: Environment = field(default_factory=Environment)

    def run(self):
        while self.environment.date < datetime.now():
            # register new users
            for _ in range(random.randint(*self.config.signups)):
                user = spawn_user(self.environment)
                self.environment.users.append(user)
                logger.info(f"New user signed up at {user.signup_date}.")

            # increment time
            self.environment.date += timedelta(days=1)


def spawn_user(environment: Environment):
    return User(
        age=random.randint(18, 65),
        signup_date=environment.date + timedelta(minutes=random.randint(0, 24 * 60)),
        coverage=random.uniform(0, 1),
        profile=random.choice(environment.profiles),
    )
