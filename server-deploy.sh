#!/bin/bash

git pull

bundle exec jekyll build

rm -rf ../htdocs/*

cp -r _site/* ../htdocs