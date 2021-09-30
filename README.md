# Introduction

This repo is to get information for pokeapi using name or id or the pokemon

# Installation Guide

1. clone repo
2. pip install -r requirements.txt
3. key in python app.py to start running and follow the instruction

## Architechure

- storing searched info in db.txt to cache result for frequent usage

### App cycle

1. when app is started, create db.txt if it does not exist, else load db.txt to memory
2. start taking requests from users, show some guide for sample user input
3. repeat until user ends application

