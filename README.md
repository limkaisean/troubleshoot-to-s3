# Troubleshoot-to-s3

This project enables uploading data from preflight checks and support-bundle generation using [Troubleshoot.sh](https://github.com/replicatedhq/troubleshoot).

## Getting Started

1. Clone this repo.
```sh
git clone https://github.com/limkaisean/troubleshoot-to-s3.git
```
2. Create `.env` and fill in the AWS credentials. For example,
```sh
AWS_DOMAIN=your_domain
AWS_BUCKET_NAME=your_bucket_name
AWS_ACCESS_KEY=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```
3. Run `docker-compose up` to start up the container.

4. Head towards `http://127.0.0.1:5000/`.
