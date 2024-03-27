# Semantic Search + NER Demo

Built following the excellent [blog post by Camille Corti-Georgiou](https://www.elastic.co/search-labs/blog/articles/developing-an-elastic-search-app-with-streamlit-semantic-search-and-named-entity-extraction).

Uses [Poetry](https://python-poetry.org) for dependancies management, and [streamlit](https://streamlit.io/) for the web interface.

Once you've installed the dependencies, you can run the app with `poetry run semantic_ner_search_demo`. This will launch the web interface, which will be available at `http://127.0.0.1:8501/`.

## Docker

You can also run the app using [Docker](https://docs.docker.com/get-docker/).

## Building the container

First, build the docker container. There is a Dockerfile in the root of the repository. You can use `docker` or `docker-compose`:

```sh
# docker
DOCKER_BUILDKIT=1 docker build -f Dockerfile --target runtime -t face0b1101/semantic-ner-search-demo:0.1 .

# docker-compose
docker-compose build
```

Once the container is built, you can run it with:

```shell
# docker
docker run --rm --name demo --env-file .env -p 8501:8501 face0b1101/semantic-ner-search-demo:0.1

# docker-compose
docker-compose up
```

This runs the container and exposes port 8501 on the host.
