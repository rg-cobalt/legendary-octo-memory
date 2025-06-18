# legendary-octo-memory
Example Repository for Semgrep CE CI/CD

# Vulnerable Python App

This intentionally vulnerable Flask app is for testing static analysis tools like Semgrep.

**Do not deploy this code. It is insecure by design.**

## Example Vulnerabilities

- SQL Injection (`routes.py`)
- Unsafe use of `eval` and `subprocess`
- Hardcoded secrets (`config.py`)
- Flask debug mode enabled
