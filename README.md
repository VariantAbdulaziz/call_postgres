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
    ParameterKey=PgHost,ParameterValue=<PgHost> \
    ParameterKey=PgPort,ParameterValue=5432 \
    ParameterKey=PgDbName,ParameterValue=<PgDbName> \
    ParameterKey=PgUser,ParameterValue=<PgUser> \
    ParameterKey=PgPassword,ParameterValue=<PgPassword>
```
