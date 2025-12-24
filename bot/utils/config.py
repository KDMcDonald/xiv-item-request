import keyring as kr


guild_id : list = []

def get_token(service_name : str, username : str) -> str | None:
    '''
    Gets the token from the system's key storage system.

    Args:
        service_name (str) : The name of the service for the key store.
        username (str) : The username, or name, of the token in the service's key store.

    Return:
        (str | None) : If the service has a token by the name, it will return the token. Otherwise returns None.
    '''
    return kr.get_password(service_name=service_name, username=username)

def assign_guild_id(id : int) -> None:
    guild_id.append(id)
