# main.py

from fastapi import FastAPI, HTTPException
import uvicorn
import math

app = FastAPI(
    title="Prime Number Checker API",
    description="API to check if a number is prime or not",
    version="1.0.0",
)

def is_prime(n: int) -> bool:
    """Determines if a positive integer 'n' is a prime number."""
    if n < 1:
        return False
    # 2 and 3 are prime numbers 
    if n <=3:
        return True
    # if divisible by 2 or 3, it's not prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # check for other divisors up to the square root of n
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# --- FastAPI Endpoints ---

@app.get("/")
def read_root():
    """Root endpoint for service health check and general info."""
    return {"message": "Welcome to the Prime Checker Microservice! Use the /check/{number} endpoint."}

@app.get("/prime/{number}", tags=["Prime Checker"])
def check_prime(number: int):
    """
    Endpoint to check if the given integer is a prime number.
    - **number**: The integer to check for primality.
    """

    if number < 2:
        raise HTTPException(status_code=400, detail="Number must be greater than 1")
    
    result = is_prime(number)
    
    return {
        "number": number,
        "is_prime": result,
        "message": "Number is prime" if result else "Number is not prime"
    }

@app.get("/health", tags=["Health Check"])
def health_check():
    """Endpoint for health check."""
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
