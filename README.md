# opyapi
Opyapi is a python framework build around [Open API](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#dataTypes) 
specification to provide toolset for rapid REST api development.

## Beauty of opyapi
No bloat. Just code. 

### Features
  - Automated documentation generation
  - Routing
  - Mock server
  - Built-in serialization/deserialization mechanisms
  - WSGI compatibility


## Quick start

```python
from opyapi import annotations
from opyapi import TextResponse


@annotations.Api(
    title="Example rest application",
    description="This application greets users",
)
class Application:
    pass


@annotations.Operation(
    "/users/{name}",
    method="get",
    responses=TextResponse(200),
    summary="Says hello with username provided in the route"
)
def hello_user(name: str):
    return f"Hello {name}"

```

## Running application

## Schema

### Supported types

#### Boolean
#### String
#### Integer
#### Number
#### Array
#### Object


## Input handling


## Working with output


## Generating documentation


## Related specs
[Open api specs](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#dataTypes)


[Json schema specs](http://json-schema.org/latest/json-schema-validation.html)
