# Variabili per la funzione Lambda
variable "lambda_function_name" {
  description = "Nome della funzione Lambda"
  type        = string
  default     = "german_phone_parser_lambda"
}

variable "lambda_handler" {
  description = "Handler della funzione Lambda"
  type        = string
  default     = "lambda_function.lambda_handler"
}

variable "lambda_runtime" {
  description = "Runtime della funzione Lambda"
  type        = string
  default     = "python3.8"
}

variable "lambda_timeout" {
  description = "Timeout della funzione Lambda"
  type        = number
  default     = 60
}

variable "lambda_memory_size" {
  description = "Dimensione della memoria della funzione Lambda"
  type        = number
  default     = 256
}
