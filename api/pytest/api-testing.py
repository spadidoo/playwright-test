# ----- Documentation -----
# - Run this test using: pytest todo-app-test.py
# - APIRequestContext -> https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-post
# - Python F Strings -> https://realpython.com/python-f-strings/https://realpython.com/python-f-strings/
# - Pytest Fixtures -> https://playwright.dev/python/docs/test-runners#fixtures
# - Python Function Annotations -> https://peps.python.org/pep-3107/
# - Typing: https://docs.python.org/3/library/typing.html
# -------------------------

"""
Generic API Testing Suite - Works with any REST API
Follows CRUD pattern: Create → Read → Update → Delete

This module provides automated testing for API endpoints using Playwright and Pytest.
It demonstrates how to test the complete lifecycle of a resource.
"""

from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="module")
def resource_ids():
    """
    Fixture: Stores resource IDs created during tests
    
    Scope: module - exists for the entire test module
    Yields: empty list that gets populated with created IDs
    """
    ids = []
    yield ids


@pytest.fixture(scope="session")
def api_client(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    """
    Fixture: Sets up HTTP client for making API requests
    
    Scope: session - exists for the entire test session (reused across all tests)
    Args: playwright - automatically injected by pytest
    Yields: APIRequestContext object for making HTTP calls
    Finally: Disposes/closes the client after all tests complete
    """
    client = playwright.request.new_context(base_url="http://localhost:3000")
    yield client
    client.dispose()


def test_create_resource(api_client: APIRequestContext, resource_ids) -> None:
    """
    CREATE Test: Send POST request to create a new resource
    
    HTTP Method: POST
    Endpoint: /todos
    Purpose: Add a new resource to the API
    """
    # Define the payload (data) to send in the request
    payload = {
        "completed": False,
        "title": "test from playwright",
        "id": "500",
    }
    
    # Send HTTP POST request with the payload
    response = api_client.post("/todos", data=payload)
    
    # Assert that the response status is successful (2xx status code)
    assert response.ok, f"Creation failed: {response.status_text}"
    
    # Convert response body to dictionary
    created_resource = response.json()
    
    # Save the created ID for use in subsequent tests
    resource_ids.append(created_resource['id'])
    
    # Print the response for debugging
    print(f"Created resource: {created_resource}")


def test_read_resource(api_client: APIRequestContext, resource_ids) -> None:
    """
    READ Test: Send GET request to retrieve a resource
    
    HTTP Method: GET
    Endpoint: /todos/{id}
    Purpose: Fetch and verify the created resource exists
    """
    # Get the ID from the list created in the previous test
    resource_id = resource_ids[0]
    
    # Send HTTP GET request to retrieve the resource
    response = api_client.get(f"/todos/{resource_id}")
    
    # Assert that the response status is successful
    assert response.ok, f"Retrieval failed: {response.status_text}"
    
    # Convert response to dictionary
    resource_data = response.json()
    
    # Validate the retrieved data matches what we created
    assert resource_data['title'] == "test from playwright"
    assert resource_data['completed'] == False
    
    # Print the response for debugging
    print(f"Retrieved resource: {resource_data}")


def test_update_resource(api_client: APIRequestContext, resource_ids) -> None:
    """
    UPDATE Test: Send PATCH request to modify a resource
    
    HTTP Method: PATCH
    Endpoint: /todos/{id}
    Purpose: Update specific fields of an existing resource
    Note: PATCH sends only the fields to update (partial update)
    """
    # Get the ID from the list
    resource_id = resource_ids[0]
    
    # Define only the fields to update
    updates = {"completed": True}
    
    # Send HTTP PATCH request with the updates
    response = api_client.patch(f"/todos/{resource_id}", data=updates)
    
    # Assert that the response status is successful
    assert response.ok, f"Update failed: {response.status_text}"
    
    # Convert response to dictionary
    updated_resource = response.json()
    
    # Validate the update was applied
    assert updated_resource['completed'] is True
    
    # Print the response for debugging
    print(f"Updated resource: {updated_resource}")


def test_delete_resource(api_client: APIRequestContext, resource_ids) -> None:
    """
    DELETE Test: Send DELETE request to remove a resource
    
    HTTP Method: DELETE
    Endpoint: /todos/{id}
    Purpose: Remove the resource from the API
    """
    # Get the ID from the list
    resource_id = resource_ids[0]
    
    # Send HTTP DELETE request to remove the resource
    response = api_client.delete(f"/todos/{resource_id}")
    
    # Assert that the response status is successful
    assert response.ok, f"Deletion failed: {response.status_text}"
    
    # Convert response to dictionary (API may return deleted object)
    deleted_resource = response.json()
    
    # Print the response for debugging
    print(f"Deleted resource: {deleted_resource}")