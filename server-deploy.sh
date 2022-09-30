#!/bin/bash

bundle exec jekyll build

rm -rf ../htdocs/*

cp -r _site/* ../htdocs