output "lambda_function_arn" {
  description = "ARN della funzione Lambda"
  value       = aws_lambda_function.german_phone_parser_lambda.arn
}

output "api_gateway_url" {
  description = "URL dell'API Gateway"
  value       = aws_api_gateway_deployment.german_phone_deployment.invoke_url
}
