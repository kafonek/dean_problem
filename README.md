_Work in Progress_

This is a small exploratory project based on a conversation with Dean M about a weekly Python/SQL problem. Given a small dataset of animal weights and which zoo they are in, craft a SQL query to find the second heaviest animal at each zoo.

In this scratchpad repo, I'm using some database ingest and query syntax that is common to building FastAPI apps, namely having a `models.py` for SQLAlchemy models and `schemas.py` for Pydantic models. Normally I'd also have a `database.py` to handle creating the SQLAlchemy `Session` but in this case I'm just creating it in each Notebook so that it's easier to turn `echo=True` on and off.

Running `notebooks/Cleaning Data.ipynb` isn't necessary since the `zoo_animals.db` is part of this repo. You are welcome to delete `zoo_animals.db` and rerun that Notebook to recreate the database.
