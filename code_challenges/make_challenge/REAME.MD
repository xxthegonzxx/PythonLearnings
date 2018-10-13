# Makefile Challenge

The challenge was to create a Python script that would be able to request a specific configuration from a `config.json` file.
The Makefile was included to package up the `app.py` file and upload it to a test s3 bucket depending on which git branch you were on.

## Makefile Usage

Tars up the `app.py` script and uploads it to a sample s3 bucket. The title of the upload is dependent on the enviroment (`dev/demo/prod`).

`$make -B dev`
`$make -B demo`
`$make -B prod`