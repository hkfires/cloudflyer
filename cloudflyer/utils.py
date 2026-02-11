import httpx

def get_free_port(host='127.0.0.1'):
    """
    Get an available free port on the specified IP address
    
    Args:
        ip (str): IP address, defaults to localhost '127.0.0.1'
        
    Returns:
        int: Available port number
    """
    import socket
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Set port to 0 to let the system assign a random free port
        sock.bind((host, 0))
        # Get the assigned port number
        _, port = sock.getsockname()
        return port
    finally:
        sock.close()

async def test_proxy(proxy_config: dict):
    """
    Test the connectivity of a proxy.

    Args:
        proxy_config (dict): A dictionary containing proxy details (scheme, host, port, username, password).

    Raises:
        Exception: If the proxy test fails.
    """
    scheme = proxy_config['scheme']
    host = proxy_config['host']
    port = proxy_config['port']
    username = proxy_config.get('username')
    password = proxy_config.get('password')

    if username and password:
        proxy_url = f"{scheme}://{username}:{password}@{host}:{port}"
    else:
        proxy_url = f"{scheme}://{host}:{port}"

    async with httpx.AsyncClient(proxy=proxy_url) as client:
        await client.get("https://httpbin.org/get", timeout=10)
