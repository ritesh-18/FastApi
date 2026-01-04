# Lets talk about docker , how it is useful for building a ml project

### Whai is Docker ? - is a platform designed to help developers build , share , and run container applications.

- Why do we need Dockers?

  - Consistency Across Environments

          - Problem : Applications often behave differently in dev , prod , testing env. due to variants in configurations , dependencies , and infrastructure.
          - Solution : Docker provides isolated environments for each applications , preventing interference and ensuring stable performance.

  - Isolation

    - Problem: Running multiple applications on the same host can lead to conflicts , such as dependecy clashes or resources contention.
    - Solution : Docker provides isolated environments for each applications , preventing interference and ensuring stable performance.

  - Scalability
    - Problem : Scaling applications to handle increased load can e challenging , requiring manual intervention and configuration.
    - Solution : Docker makes it easy to scale application horizonatlly by running multiple sontainer instances allowing for quick and effcient scaling.

## How exacatly docker is used ?

- Docker Engine
  - Docker Engine is the core component of the Docker platform, responsible for creating,
    running, and managing Docker containers. It serves as the runtime that powers Docker's
    containerization capabilities. Here’s an in-depth look at the Docker Engine:
- Components of Docker Engine

1. Docker Daemon (dockerd):
 - Function: The Docker daemon is the background service running on the host machine. It manages Docker objects such as images, containers, networks, and volumes.

 - Interaction: It listens for Docker API requests and processes them, handling container lifecycle operations (start, stop, restart, etc.).

2. Docker CLI (docker):
 - Function: The Docker Command Line Interface (CLI) is the tool that users interact with to communicate with the Docker daemon.

 - Usage: Users run Docker commands through the CLI to perform tasks like building images, running containers, and managing Docker resources.

3. REST API:
 - Function: The Docker REST API allows communication between the Docker CLI and the Docker daemon. It also enables programmatic interaction with Docker.

 - Usage: Developers can use the API to automate Docker operations or integrate Docker functionality into their applications.



 .... There are so many components related to docker
      -- i have added one pdf that contains all the details related to docker

### How to pull an image :
- cmd: docker pull <image-name>
- How to run this image :
     - docker run <image-name>
     - docker run -p portno:portno <image-name> 

- How to build a docker image :
     - docker build -t <user_name/name-image>  . 
     - dot(.) at the end is required to buildinside the same folder(project directory)   
      - how to run this image :
         docker run -p outside_port:docker_image_port <image name>


### How to deploy docker image on AWS:
 - ![alt text](<Screenshot from 2026-01-04 19-36-30.png>)

##### Pdf credit : Campus X (yt-channel)     




