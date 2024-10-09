# Basics of HTTP/HTTPS

# Basics of HTTP/HTTPS

## HTTP (HyperText Transfer Protocol)
- **Definition**: HTTP is a protocol used for transmitting hypertext over the internet.
- **Port**: Typically uses port 80.
- **Security**: Data is transmitted in plain text, making it vulnerable to interception and attacks.
- **Use Case**: Suitable for non-sensitive data transmission where security is not a primary concern.

## HTTPS (HyperText Transfer Protocol Secure)
- **Definition**: HTTPS is an extension of HTTP that uses encryption to secure data transmission.
- **Port**: Typically uses port 443.
- **Security**: Data is encrypted using SSL/TLS, providing confidentiality, integrity, and authentication.
- **Use Case**: Essential for transmitting sensitive data such as login credentials, payment information, and personal details.

### Key Differences
1. **Security**: HTTP is not secure, while HTTPS provides a secure communication channel.
2. **Port**: HTTP uses port 80, whereas HTTPS uses port 443.
3. **Encryption**: HTTP transmits data in plain text, while HTTPS encrypts data using SSL/TLS.
4. **Trust**: HTTPS requires a digital certificate from a trusted Certificate Authority (CA), ensuring the authenticity of the website.

In summary, HTTPS is the secure version of HTTP, providing encryption and authentication to protect data during transmission.
