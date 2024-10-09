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

