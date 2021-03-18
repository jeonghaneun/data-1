#!/bin/bash
docker run -it \
              --name harry-potter \
              --rm \
              -v $(pwd)/test:/app \
              test:0.3

