# Databeat

Welcome to Databeat, an elastic beat to gather data from SQL data sources and feed it to elasticsearch.


## Getting Started with Databeat

Ensure that this folder is at the following location:
`${GOPATH}/github.com/bhazard/databeat`

### Requirements

* [Golang](https://golang.org/dl/) 1.7

### Init Project
To get running with Databeat and also install the
dependencies, run the following command:

```
make setup
```

For further development, check out the [beat developer guide](https://www.elastic.co/guide/en/beats/libbeat/current/new-beat.html).

### Build

To build the binary for Databeat run the command below. This will generate a binary
in the same directory with the name databeat.

```
make
```


### Run

To run Databeat with debugging output enabled, run:

```
./databeat -c databeat.yml -e -d "*"
```


### Test

To test Databeat, run the following command:

```
make testsuite
```

alternatively:
```
make unit-tests
make system-tests
make integration-tests
make coverage-report
```

The test coverage is reported in the folder `./build/coverage/`

### Update

Each beat has a template for the mapping in elasticsearch and a documentation for the fields
which is automatically generated based on `etc/fields.yml`.
To generate etc/databeat.template.json and etc/databeat.asciidoc

```
make update
```


### Cleanup

To clean  Databeat source code, run the following commands:

```
make fmt
```

To clean up the build directory and generated artifacts, run:

```
make clean
```


### Clone

To clone Databeat from the git repository, run the following commands:

```
mkdir -p ${GOPATH}/github.com/bhazard/databeat
cd ${GOPATH}/github.com/bhazard/databeat
git clone https://github.com/bhazard/databeat
```


For further development, check out the [beat developer guide](https://www.elastic.co/guide/en/beats/libbeat/current/new-beat.html).


## Packaging

The beat frameworks provides tools to crosscompile and package your beat for different platforms. This requires [docker](https://www.docker.com/) and vendoring as described above. To build packages of your beat, run the following command:

```
make package
```

This will fetch and create all images required for the build process. The hole process to finish can take several minutes.
