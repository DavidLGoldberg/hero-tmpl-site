#!/bin/bash
watchr -e 'watch(".*\.less$$") { |f| system("lessc less/style.less /public/css/style.css") }' &
