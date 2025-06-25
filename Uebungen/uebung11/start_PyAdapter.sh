#!/bin/sh

java -version
java -cp "lib/adv-lib-2.1.jar:lib/adv-util-2.0.jar:lib/python_adapter.jar"  --add-opens java.base/java.lang=ALL-UNNAMED uebung11/ml/aufgabe02/PythonAdapterDFS
