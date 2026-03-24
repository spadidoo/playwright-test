# ====================================================================
# GENERALIZED API TESTING WITH PLAYWRIGHT
# ====================================================================
# This script demonstrates how to make HTTP requests to ANY API
# and test the response using Playwright's APIRequestContext
# ====================================================================

import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    """
    Main function to perform API testing
    
    Args:
        playwright: Playwright instance for making API requests
    """
    
    # STEP 1: Create an API request context
    # ====================================================================
    # This creates a connection to your API server
    # Change 'base_url' to any API endpoint (localhost, remote, etc.)
    # Examples:
    #  - "http://localhost:3000" (your local development app)
    #  - "https://api.github.com" (GitHub API)
    #  - "https://jsonplaceholder.typicode.com" (free public API for testing)
    # ====================================================================
    api_request_context = await playwright.request.new_context(
        base_url="https://api.example.com"  # ← CHANGE THIS to your API URL
    )
    
    # STEP 2: Prepare the data/payload to send
    # ====================================================================
    # Create a dictionary with the data fields required by your API
    # The structure depends on what the API expects
    # "key": value pairs must match your API's requirements
    # These are PLACEHOLDERS - adjust for your specific API
    # ====================================================================
    request_payload = {
        "field_one": "some_value",      # ← Replace with actual field
        "field_two": False,             # ← Replace with actual field
        "field_three": 123,             # ← Replace with actual field
    }
    
    # STEP 3: Send an HTTP POST request
    # ====================================================================
    # POST = Create something new (like submitting a form)
    # The endpoint path is relative to your base_url
    # Examples:
    #  - "/todos" creates at https://api.example.com/todos
    #  - "/users" creates at https://api.example.com/users
    #  - "/api/products" creates at https://api.example.com/api/products
    # ====================================================================
    response = await api_request_context.post(
        "/endpoint_path",        # ← CHANGE THIS to your API endpoint
        data=request_payload,    # ← Send the data as request body
    )
    
    # STEP 4: Validate the response
    # ====================================================================
    # response.ok returns True if status code is 200-299 (success)
    # If it fails, the assertion will raise an error and stop execution
    # HTTP Status Codes:
    #  - 200-299: Success ✓
    #  - 400: Bad Request ✗
    #  - 401: Unauthorized ✗
    #  - 404: Not Found ✗
    #  - 500: Server Error ✗
    # ====================================================================
    assert response.ok, f"API request failed with status: {response.status}"
    
    # STEP 5: Extract and display the result
    # ====================================================================
    # response.json() converts the API's response to a Python dictionary
    # This allows you to access and verify the returned data
    # Example: result['id'] or result['message']
    # ====================================================================
    result = response.json()
    print(f"✓ API Response received:")
    print(f"  Status Code: {response.status}")
    print(f"  Response Data: {result}")

async def main():
    """
    Entry point for async execution
    
    This function:
    1. Starts a Playwright session
    2. Calls the run() function
    3. Cleans up resources when done
    """
    async with async_playwright() as playwright:
        await run(playwright)

# STEP 6: Execute the script
# ====================================================================
# asyncio.run() starts the async event loop and runs main()
# This is required to run async code in Python
# ====================================================================
asyncio.run(main())