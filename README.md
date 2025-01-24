# lad-api-practice
Repository dedicated to hosting the source code for multiple APIs developed using different technologies.

## Running the Lambda Function Locally

1. **Install AWS SAM CLI**: Ensure you have the AWS SAM CLI installed. You can download it from the [official AWS SAM CLI page](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

2. **Build the SAM Application**:

   ```sh
   sam build
   ```

3. **Start the API locally**:

   ```sh
   sam local start-api
   ```

4. **Test the API locally**:

   ```sh
   curl http://localhost:3000/lad-api-practice-dev/hello
   ```

## Packaging and Deploying the SAM Application

1. **Package the SAM Application**:

   ```sh
   sam package
   ```

2. **Deploy the SAM Application**:

   ```sh
   sam deploy
   ```

3. **Test the deployed API**:

   ```sh
   curl --location 'https://p2woq879j6.execute-api.us-east-1.amazonaws.com/Prod/lad-api-practice-dev/hello'
   ```
