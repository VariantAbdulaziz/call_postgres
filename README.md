# Local Development & Testing

---

## 1. Build the Application

```bash
sam build --use-container
```

## 2. edit env.json

## 3. Invoke the Lambda Function Locally

```bash
sam local invoke HelloWorldFunction --env-vars env.json --event event.json
```

# AWS Deployment

```bash
sam build

sam deploy \
  --parameter-overrides \
    ParameterKey=PG_HOST,ParameterValue=<PG_HOST> \
    ParameterKey=PG_PORT,ParameterValue=<PG_PORT> \
    ParameterKey=PG_DBNAME,ParameterValue=<PG_DBNAME> \
    ParameterKey=PG_USER,ParameterValue=<PG_USER> \
    ParameterKey=PG_PASSWORD,ParameterValue=<PG_PASSWORD>
```
