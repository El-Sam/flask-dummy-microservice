Flask dummy microservice
========================

This is my take on building a miscroservice using flask and following Domain Driven Design (DDD).

It is a dummy project describing how to setup and implement a dockerized Flask based API with a Postgresql database and Gradle integration.

This is mostly a reference for my future self.

Specs
-------

[Swagger documentation](./swagger.json)


Features
--------

- Docker containers for dev, production, command line and database.
- Gradle to automate and run frequent tasks.
- flask and python 3 to build the API
- Dependency Injection of classes' instances for easy unit testing.
- Some DDD principles
- unit testing and ~89% coverage.
- swagger documentation, manually written (still gotta figure out a good way to auto generate them).
- WSGI server setup to run the app in production env.

Usage
------------

You need to meet the following requirements so that you can run this project:
- have a Unix OS
- have docker installed and running


build the service by running: `./gradlew build`

run the api in dev mode by running: `./gradlew run`, then go then to `http://localhost:9090/persons` to see the response.

run the api in prod mode by running: `./gradlew buildProd runProd`, then go to `http://localhost:9091/persons`.

run unit tests by running: `./gradlew testUnit`

run unit tests with coverage by running: `./gradlew testCoverage`


TODO
-----

- setup CD/CI pipeline using TravisCI.
- automate swagger generation
- add contract test to test whether the API respects the contract (swagger)


Support
-------

If you are having issues or questions, please let me know, by opening an issue or send me an email [here.](sam.elaabidi@gmail.com)


License
-------

The project is licensed under the [WTFPL license](./LICENSE.txt).
