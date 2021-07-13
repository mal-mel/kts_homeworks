#!/bin/sh

docker build -t cpython-3.8 . && docker run -it cpython-3.8 /bin/bash
