def is_valid_ipv4(address: str) -> bool:
    
    if address.count('.') != 3:
        return False

    
    parts = address.split('.')
    
    
    if len(parts) != 4:
        return False

    for part in parts:
        
        if not part.isdigit():
            return False
       
        num = int(part)
        if num < 0 or num > 255:
            return False
    

    return True