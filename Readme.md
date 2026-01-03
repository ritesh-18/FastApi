# What is an API?
- An api is a mechanism that enables two software programs to communicate with each other using a defined set of rules , etc.


## Fast Api for Ml and AI
- Fast Api is modern , high performance web framework for building APIs with python.
- It is built on top of:
    - Starlette → networking + async

    - Pydantic → data validation + typing

    - webserver(uvicorn) ---> SGI(ASGI/starlette) ----> app code(python)
    - python does not support or handle async operation thats why it uses external lib like SGI to handle the req , res and converting async into python readable code.

- FastAPI is NOT a server.
    - It is just:
    - Python code
    - Routing logic
    - Validation rules  
    - does NOT listen on a port
    - does NOT accept HTTP connections
    - does NOT manage sockets
    - It only defines how to respond if a request comes.
    - In FastAPI world:
         - Uvicorn is the web server
         - Uvicorn, start a server and give requests to my FastAPI app.
         - Uvicorn handles:
            - Uvicorn is needed because FastAPI is not a web server.
            - Uvicorn listens to the network, manages connections, runs the async event loop, and executes your FastAPI app using ASGI rules.    
            - Opens TCP socket
            - Listens on a port (8000)
            - Accepts HTTP connections
            - Parses HTTP request
            - Runs an event loop
            - Calls your FastAPI app
            - Sends HTTP response back
            - Closes TCP socket

```
            Browser
            ↓
            Uvicorn (ASGI Server)
            ↓
            FastAPI (App logic)
            ↓
            Starlette (routing + middleware)
            ↓
            Your endpoint
            ↓
            Response

```

- Features of FastApi
  - FastAPI is fast, async-first, type-safe, and automatically validates data and generates API docs.
  - It removes boilerplate and lets you focus on business logic.



## Lets talk about path/ query params and how to access it 

- Path parameters are dynamic segments of a URL path used to identify a specific resource.
- In fastApi you get Path() function that is used to provide metada , validation , rules , and documentation hints for parameters in your API.

- `http_status_code` : it is a three digits code returned by a webserver (like fastApi) to indicate the result of a clients request (like from a browser or api consumer).
- They help the client (browser , frontend , etc) understand:
    - whether  the request was successfull,
    - whether something went wrong,
    - and what kind of issues occured(if any).
    - Ex: 200(success) , 201(created a resources) , 400(bad request) , 404(data not found).
- How to handle the exception :
    -raise HTTPException(status_code=404, detail="Patient ID not found")

- `Query_parameters` : are the optional key:value pairs appended at the end of url used to pass additional data to the server in an HTTP request. They are typically employed for operations like sorting , filtering , searching , and pagination , without altering the endpoint path itself.
     - ex: /patients ? city=delhi&sort_by=age
     
     - `Query()` is a utility functions provided by FastApi to declare , vlaidate , and documents query parameters in your API endpoints.
    




















### Dependencies required to create FASTAPI server
- python , pip , now create a venv : `python -m venv  myvenv` and activate it : `source myvenv/bin/activate`
- install packages : pip install fastapi uvicorn pydantic
- create a main.py file and add the code that is presnt in main.py file
- how to run main.py :
    - using uvicorn web server
    - uvicorn <file_name>:<fastapi_obj_name> --reload  

### Recommended FastApi Microservice folder structure

```
        user-service/
        │
        ├── app/
        │   ├── main.py                 # App entry point (like main.ts)
        │   │
        │   ├── api/                    # API layer (routes/controllers)
        │   │   ├── v1/
        │   │   │   ├── __init__.py
        │   │   │   ├── routes.py       # Router aggregation
        │   │   │   └── users.py        # User endpoints
        │   │
        │   ├── core/                   # Core app configuration
        │   │   ├── config.py           # Env, settings
        │   │   ├── security.py         # JWT, auth helpers
        │   │   └── logging.py          # Logging config
        │   │
        │   ├── models/                 # DB models (ORM)
        │   │   ├── __init__.py
        │   │   └── user.py
        │   │
        │   ├── schemas/                # Request / Response DTOs
        │   │   ├── __init__.py
        │   │   └── user.py
        │   │
        │   ├── services/               # Business logic
        │   │   ├── __init__.py
        │   │   └── user_service.py
        │   │
        │   ├── repositories/           # DB access layer
        │   │   ├── __init__.py
        │   │   └── user_repository.py
        │   │
        │   ├── db/                     # Database setup
        │   │   ├── base.py
        │   │   ├── session.py
        │   │   └── migrations/
        │   │
        │   ├── dependencies/           # FastAPI dependencies
        │   │   └── auth.py
        │   │
        │   ├── utils/                  # Helpers / utilities
        │   │   └── hashing.py
        │   │
        │   └── tests/                  # Unit & integration tests
        │       └── test_users.py
        │
        ├── Dockerfile
        ├── docker-compose.yml
        ├── requirements.txt
        ├── .env
        └── README.md


```
- This structure enforces separation of concerns, which is critical in microservices.
```
| Layer           | Responsibility                     |
| --------------- | ---------------------------------- |
| `api/`          | Only HTTP logic (request/response) |
| `schemas/`      | Validation & serialization         |
| `services/`     | Business rules                     |
| `repositories/` | DB queries                         |
| `models/`       | Database schema                    |
| `core/`         | App-wide config                    |
| `db/`           | Connection & migrations            |

```
- For real microservice setups, you should also add:

```
app/
├── messaging/        # Kafka / RabbitMQ
├── clients/          # Call other services
├── middlewares/      # Request tracing, metrics
├── health/           # /health, /readiness


```