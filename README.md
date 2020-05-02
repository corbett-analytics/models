# Corbett Models

Free to use, example models deployed at `models.corbettanalytics.com`. You can also use this repo as a skeleton for deploying more complex models to AWS lambda.

## Deploying

Make sure that your `~/.aws/credentials` file includes access keys that have admin permissions for your AWS account.

Install dependencies.

```
pip install -r requirements.txt
```

Train the models.

```
python train.py
```

Push updates to the lambda functions.

```
zappa udpate
```
