#!/usr/bin/env bash
docker build -f Dockerfile.bot --tag botbrown:0.1 --tag botbrown:latest .
docker build -f Dockerfile.ment --tag botment:0.1 --tag botment:latest .
