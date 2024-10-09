# Basics of HTTP/HTTPS

# Basics of HTTP/HTTPS

## HTTP (HyperText Transfer Protocol)
- **Definition**: HTTP is a protocol used for transmitting hypertext over the internet. It is the foundation of any data exchange on the Web and it is a protocol used for fetching resources such as HTML documents.
- **Port**: Typically uses port 80.
- **Security**: Data is transmitted in plain text, making it vulnerable to interception and attacks. This means that any data sent over HTTP can be read by anyone who intercepts the communication.
- **Use Case**: Suitable for non-sensitive data transmission where security is not a primary concern. Commonly used for websites where security is not a major issue, such as blogs or informational sites.

## HTTPS (HyperText Transfer Protocol Secure)
- **Definition**: HTTPS is an extension of HTTP that uses encryption to secure data transmission. It ensures that data sent between the client and server is encrypted and secure from eavesdroppers.
- **Port**: Typically uses port 443.
- **Security**: Data is encrypted using SSL/TLS, providing confidentiality, integrity, and authentication. This means that even if the data is intercepted, it cannot be read without the decryption key.
- **Use Case**: Essential for transmitting sensitive data such as login credentials, payment information, and personal details. It is used by websites that require secure communication, such as online banking, email services, and e-commerce sites.

### Key Differences
1. **Security**: HTTP is not secure, while HTTPS provides a secure communication channel by encrypting data.
2. **Port**: HTTP uses port 80, whereas HTTPS uses port 443.
3. **Encryption**: HTTP transmits data in plain text, while HTTPS encrypts data using SSL/TLS, making it unreadable to unauthorized parties.
4. **Trust**: HTTPS requires a digital certificate from a trusted Certificate Authority (CA), ensuring the authenticity of the website and establishing a secure connection.

In summary, HTTPS is the secure version of HTTP, providing encryption and authentication to protect data during transmission. It is crucial for any website that handles sensitive information to use HTTPS to ensure the security and privacy of its users.

---------------------------------

## HTTP/2 Request and Response Structure

### HTTP/2 Request
An HTTP/2 request consists of the following components:
- **:method**: The HTTP method (e.g., GET, POST).
- **:scheme**: The scheme of the target URL (e.g., https).
- **:authority**: The authority of the target URL (e.g., www.example.com).
- **:path**: The path of the target URL (e.g., /index.html).
- **Headers**: Additional metadata about the request (e.g., User-Agent, Accept).
- **Body**: The payload of the request, used with methods like POST and PUT.

Example:
```
:method: GET
:scheme: https
:authority: www.example.com
:path: /index.html
user-agent: Mozilla/5.0
accept: text/html
```

### HTTP/2 Response
An HTTP/2 response consists of the following components:
- **:status**: The HTTP status code (e.g., 200, 404).
- **Headers**: Metadata about the response (e.g., Content-Type, Content-Length).
- **Body**: The payload of the response, which is the actual content being returned.

Example:
```
:status: 200
content-type: text/html
content-length: 1234

<html>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
```

### Key Features of HTTP/2
1. **Multiplexing**: Multiple requests and responses can be sent over a single connection simultaneously.
2. **Header Compression**: HTTP/2 uses HPACK compression to reduce the size of headers.
3. **Stream Prioritization**: Clients can assign priority levels to streams, allowing more important resources to be loaded first.
4. **Server Push**: Servers can send resources to clients proactively, without waiting for them to be requested.

In summary, HTTP/2 enhances the performance and efficiency of web communication by introducing features like multiplexing, header compression, and server push, making it a significant improvement over HTTP/1.1.

-----------------------


## Common HTTP Methods

### GET
- **Description**: Retrieves data from the server.
- **Use Case**: Fetching a web page or data from an API.

### POST
- **Description**: Submits data to be processed to a specified resource.
- **Use Case**: Submitting form data or uploading a file.

### PUT
- **Description**: Updates a current resource with new data.
- **Use Case**: Updating user information or modifying a resource.

### DELETE
- **Description**: Deletes a specified resource.
- **Use Case**: Removing a user account or deleting a file.

### PATCH
- **Description**: Applies partial modifications to a resource.
- **Use Case**: Updating a single field in a user profile.

### HEAD
- **Description**: Similar to GET but only retrieves the headers.
- **Use Case**: Checking if a resource exists without downloading it.

### OPTIONS
- **Description**: Describes the communication options for the target resource.
- **Use Case**: Determining the HTTP methods supported by a server.

### CONNECT
- **Description**: Establishes a tunnel to the server identified by the target resource.
- **Use Case**: Used for SSL tunneling.

### TRACE
- **Description**: Performs a message loop-back test along the path to the target resource.
- **Use Case**: Debugging and diagnostic purposes.

## Common HTTP Status Codes

### 200 OK
- **Description**: The request has succeeded.
- **Scenario**: When a web page or resource is successfully retrieved.

### 201 Created
- **Description**: The request has been fulfilled and resulted in a new resource being created.
- **Scenario**: When a new user account is created.

### 204 No Content
- **Description**: The server successfully processed the request, but is not returning any content.
- **Scenario**: When a resource is deleted.

### 400 Bad Request
- **Description**: The server could not understand the request due to invalid syntax.
- **Scenario**: When required parameters are missing in a request.

### 401 Unauthorized
- **Description**: The client must authenticate itself to get the requested response.
- **Scenario**: When accessing a protected resource without valid credentials.

### 403 Forbidden
- **Description**: The client does not have access rights to the content.
- **Scenario**: When trying to access a restricted area without proper permissions.

### 404 Not Found
- **Description**: The server can not find the requested resource.
- **Scenario**: When a requested page or resource isn’t available on the server.

### 500 Internal Server Error
- **Description**: The server has encountered a situation it doesn't know how to handle.
- **Scenario**: When an unexpected condition was encountered on the server.

### 502 Bad Gateway
- **Description**: The server was acting as a gateway or proxy and received an invalid response from the upstream server.
- **Scenario**: When a server is down or there is a network error.

### 503 Service Unavailable
- **Description**: The server is not ready to handle the request.
- **Scenario**: When the server is undergoing maintenance or is overloaded.
