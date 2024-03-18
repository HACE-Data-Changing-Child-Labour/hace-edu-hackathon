## HACE Hackathon Starter Project

This is a starter project for the HACE Hackathon.
It aims to provide a basic implementation for accessing articles from a database.

You should use this project as a starting point for your hackathon project.

## Setup

This quick guide will help you get started with the project.

### Prerequisites

You will need the following things installed to run this project:

* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

It may also be helpful to have the following installed:

* [Python Language Server](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (for Visual Studio Code)

### Getting Started

To get started, you should clone this repository with the following command:

```bash
git clone https://github.com/HACE-Data-Changing-Child-Labour/hace-edu-hackathon.git
```

Then, you should navigate to the project directory:

```bash
cd hace-edu-hackathon
```

You will then need to create a `.env` file in the root of the project directory.
This file should contain the following environment variables:

```bash
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
S3_BUCKET_PATH=your_s3_bucket
```
You will be provided with these credentials during the hackathon.

The project can be started with the following command:

```bash
make start
```

This will then run the project via a Docker container.
If you wish to turn this starter into a service for some reason, the default exposed port is 3000.

You can install new dependencies by adding them to the `requirements.txt` file and running the following command:

```bash
make build
```

This will then rebuild the Docker container with the new dependencies.

### Resolving Issues

If you run into some issues during the prequisite installation, let me know and I can help you out.

If you run into issues with Docker, you can try the following:

Run the following command to do a clean up of the Docker resources:

```bash
make clean
```

If you're still stuck, let me know and I can help you out.


## Tasks

The following are the proposed tasks for the hackathon:

1. **Entity Extraction: Location**:
    Entity extraction from our data set of news articles related to child labour, where entities are countries/ locations. Can you visualise the extracted location entities on a map?

2. **Entity Extraction: Companies**: 
    Entity extraction from our data set of news articles related to child labour, where entities are companies.


3. **Entity Extraction: Commodities**:
    Entity extraction from our data set of news articles related to child labour, where entities are commodities.


