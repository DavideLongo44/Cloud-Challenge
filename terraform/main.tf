# provider AWS specifica la regione AWS da utilizzare
provider "aws" {
  region = "us-east-1"  # Set the appropriate AWS region
}

# Crea un ruolo IAM per le funzioni Lambda
# Create an IAM role for Lambda functions
resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      Action    = "sts:AssumeRole"
    }]
  })
}

# Attacca una politica IAM al ruolo per consentire l'accesso a CloudWatch Logs
# Attach an IAM policy to the role to allow access to CloudWatch Logs
resource "aws_iam_policy_attachment" "lambda_logs_attachment" {
  name       = "lambda_logs_attachment"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  roles      = [aws_iam_role.lambda_role.name]
}

# Crea una funzione Lambda
# Create a Lambda function
resource "aws_lambda_function" "german_phone_parser_lambda" {
  function_name    = "german_phone_parser_lambda"
  filename         = "path/to/your/lambda_function.zip"
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.8"
  role             = aws_iam_role.lambda_role.arn
  timeout          = 60
  memory_size      = 256
}

# Crea un'API Gateway
# Create an API Gateway
resource "aws_api_gateway_rest_api" "german_phone_api" {
  name        = "german_phone_api"
  description = "API for German phone numbers parser"
}

# Crea una risorsa API Gateway
# Create an API Gateway resource
resource "aws_api_gateway_resource" "german_phone_resource" {
  rest_api_id = aws_api_gateway_rest_api.german_phone_api.id
  parent_id   = aws_api_gateway_rest_api.german_phone_api.root_resource_id
  path_part   = "parse"
}

# Crea un metodo API Gateway POST
# Create an API Gateway POST method
resource "aws_api_gateway_method" "german_phone_method" {
  rest_api_id   = aws_api_gateway_rest_api.german_phone_api.id
  resource_id   = aws_api_gateway_resource.german_phone_resource.id
  http_method   = "POST"
  authorization = "NONE"
}

# Collega il metodo API Gateway alla funzione Lambda
# Link the API Gateway method to the Lambda function
resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id             = aws_api_gateway_rest_api.german_phone_api.id
  resource_id             = aws_api_gateway_resource.german_phone_resource.id
  http_method             = aws_api_gateway_method.german_phone_method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.german_phone_parser_lambda.invoke_arn
}

# Pubblica l'API Gateway
# Deploy the API Gateway
resource "aws_api_gateway_deployment" "german_phone_deployment" {
  depends_on = [aws_api_gateway_integration.lambda_integration]
  rest_api_id = aws_api_gateway_rest_api.german_phone_api.id
  stage_name  = "dev"
}
