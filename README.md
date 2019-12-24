# Zeit API Mock

    2019 Ondrej Sika <ondrej@ondrejsika.com>
    https://github.com/ondrejsika/zeit-api-mock

Simple [Zeit.co API](https://zeit.co/docs/api) mock for [terraform-plugin-zeit](https://github.com/ondrejsika/terraform-plugin-zeit) development.


## Install

```
git clone git@github.com:ondrejsika/zeit-api-mock.git
cd zeit-api-mock
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
