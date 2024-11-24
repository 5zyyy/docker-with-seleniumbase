### Build image
1. Open docker desktop
2. `cd <directory with Dockerfile>`
3. `docker build -t <name>:<version(optional)> .` (`.` to specify the current directory)

### Create a new container instance
`docker run <image name>`
<br>
(optional) To assign a name to the container: `docker run --name <name container> <image name>`
