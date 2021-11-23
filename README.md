# libnode 

[![release.yml workflow status](https://github.com/Kukkimonsuta/libnode/actions/workflows/release.yml/badge.svg)](https://github.com/Kukkimonsuta/libnode/actions/workflows/release.yml)

This repo contains the scripts that build [Node.js](http://nodejs.org/) as a shared library for embedding.

## Usage

### Configuring

#### Specify the Node version:
```sh
export LIBNODE_VERSION=v17.1.0
```

#### Build the x86 version (optional, Windows only):
```sh
export LIBNODE_ARCHITECTURE=x86
```

### Downloading the source code of Node.js:
```sh
python3 -m scripts.download
```

### Patch the source code:
```sh
python3 -m scripts.patch
```

### Building Node.js:
```sh
python3 -m scripts.build
```

### Postprocessing the static library files:
```sh
python3 -m scripts.postproc
```

### Copying the headers:
```sh
python3 -m scripts.headers
```

### Testing the library:
```sh
python3 -m scripts.test
```

### Archiving:
```sh
python3 -m scripts.archive
```
