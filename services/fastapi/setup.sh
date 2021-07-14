#!/bin/sh

# Call from inside K8 cluster
curl -X POST http://fastapi-service:8000/create_queue