> This repository is in **Work in Progress** state. If you need something, create an [issue](https://github.com/ondrejsika/vercel-api-mock/issues/new)

# Vercel API Mock

    2019 Ondrej Sika <ondrej@ondrejsika.com>
    https://github.com/ondrejsika/vercel-api-mock

Simple [Vercel API](https://vercel.com/docs/api) mock for [terraform-plugin-vercel](https://github.com/ondrejsika/terraform-plugin-vercel) development.

## Install

```
git clone git@github.com:ondrejsika/vercel-api-mock.git
cd vercel-api-mock
pipenv install
```

## Run

### Server

Server listen on <http://0.0.0.0:80> by defaul.

```
./run-server.sh
```

### CLI

- `./run-list-resources.sh` - list of all actual (created & not deleted) resources
