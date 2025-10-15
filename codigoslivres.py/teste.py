$body = @{
    numero = "+5519982235862"
    token = "teste"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/rastrear" -Method POST -Body $body -ContentType "application/json"