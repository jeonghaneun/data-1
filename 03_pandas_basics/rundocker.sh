#!/bin/bash
docker run -it \
              --name bunny_rabbit \
              --rm \
              -v $(pwd)/test:/app \
              -p 8888:8888 \
              -e JUPYTER_ENABLE_LAB=yes \
              pandas_basic:1.0

