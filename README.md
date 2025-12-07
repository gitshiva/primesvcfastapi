# primesvcfastapi
Microservice/API that will return if a given number is prime or not.

# CI/CD
![Build Status](https://github.com/gitshiva/primesvcfastapi/actions/workflows/ci.yml/badge.svg)

## How to run
podman build -t primesvcfastapi .  
podman run -d --name primesvcfastapi -p 8000:8000 primesvcfastapi

## How to test
http://localhost:8000/prime/171

## Everything should work :-)