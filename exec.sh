#!/usr/bin/env bash
docker build -f Dockerfile.ment --tag bottrain:0.1 --tag bottrain:latest .
docker run -v $(pwd)/data:/srv/src/data bottrain
docker build -f Dockerfile.bot --tag botbrown:0.1 --tag botbrown:latest .
docker build -f Dockerfile.ment --tag botment:0.1 --tag botment:latest .
