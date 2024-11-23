### Build image
1. Open docker desktop
2. `cd selenium-base-docker`
3. `docker build -t test-cdc-image .`

### Create and run container instance
1. Add config in `/selenium-base-docker/configs/<config name>.yaml`
2. `cd` to project root directory
3. `docker run --name <name container> -v "$(pwd)/selenium-base-docker/configs/<chosen config name>.yaml:/mounted/config.yaml" test-cdc-image`

### Note
There should be a unique config.yaml file (e.g config0.yaml, config1.yaml, config2.yaml ...) for each container.