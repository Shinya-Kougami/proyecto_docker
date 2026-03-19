target "default" {
  context = "."
  dockerfile = "Dockerfile"
  tags = ["mi-calculadora-bake:latest"]
}