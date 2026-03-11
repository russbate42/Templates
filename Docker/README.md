# Docker

The following should be an example of building a docker image on Ubuntu

```zsh
docker build -f test-rust -t test-rust .
```

This docker file is a simple test of a rust installation on Ubuntu.

Test with `docker run --rm -it test-rust /bin/bash`

Remove with `docker image rm -f hello-world`

Docker images are not files that are found in the directory, they are images
created, and verified with `docker images`

**Important**: Clean docker with `docker system prune -a --volumes`

## Ubuntu Build
```zsh
docker build -f ubuntu_nvim -r ubuntu_nvim
```

