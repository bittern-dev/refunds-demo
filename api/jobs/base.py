import time


class Job:
    """A unit of background work. Raise RetryLater from run() to try again later."""

    attempts = 3  # how many times run() is tried before giving up

    def __init__(self) -> None:
        self.tries = 0

    def run(self, *args) -> None:
        raise NotImplementedError

    def on_give_up(self, *args) -> None:
        pass

    def perform(self, *args) -> None:
        while True:
            self.tries += 1
            try:
                return self.run(*args)
            except RetryLater as e:
                if self.tries >= self.attempts:
                    return self.on_give_up(*args)
                time.sleep(e.delay)


class RetryLater(Exception):
    def __init__(self, delay: float) -> None:
        self.delay = delay


def backoff(tries: int) -> float:
    return min(60.0, 2.0**tries)
