import threading

from api.jobs.base import Job

_jobs: list[tuple[Job, tuple]] = []


def enqueue(job: Job, *args) -> None:
    _jobs.append((job, args))
    threading.Thread(target=job.perform, args=args, daemon=True).start()
