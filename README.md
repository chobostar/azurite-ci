# Azurite-ci
Example of Azurite in Docker with build-in container and HTTPS for testing and development. 

It uses self-signed certs and python provisioner.

### Why
- there is no good solution for initial provisioning:
  https://stackoverflow.com/questions/68834959/is-there-a-way-to-automatically-create-a-container-when-starting-azurite
>I've solved the issue by creating a custom docker image and executing azure-cli tools from a health check. There could certainly be better solutions, and I will update the accepted answer if someone posts a better solution.

- using curl - it's not easy too https://github.com/Azure/Azurite/issues/386
>AuthorizationFailure with curl #386

### HowTo

- See an example - [create_container.py](tests/init/create_container.py)
```
os.environ['STORAGE_CONTAINER'] = 'my-test-container'
```

- Defined certs enable `HTTPS`

### Usage
```
make up
```