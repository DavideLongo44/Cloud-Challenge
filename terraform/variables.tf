variable "lambda_function_name" {
  description = "Nome della funzione Lambda"
  type        = string
}

variable "api_gateway_name" {
  description = "Nome dell'API Gateway"
  type        = string
}

variable "dynamodb_table_name" {
  description = "Nome della tabella DynamoDB"
  type        = string
}

variable "iam_role_name" {
  description = "Nome del ruolo IAM"
  type        = string
}
