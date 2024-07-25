import re
from typing import Optional

def _check_is_numeric(string) -> tuple[bool, Optional[str]]:
    """
    Cheks if `string` is an isinstance of common int or float.
    Return tuple(bool, str or None) based on results.
    
    Example:
        
        .. code-block:: python
        
            examples = [
                35, 92.4, '64', '95.8', '99,36',
                'string', '89r8', '.84', '48.689,844'
            ]
            
            for string in examples:
                print(_check_is_numeric(string))
        
        .. output:: console
            >> (True, '35')
            >> (True, '92.4')
            >> (True, '64')
            >> (True, '95.8')
            >> (True, '99.36')
            >> (False, None)
            >> (False, None)
            >> (False, None)
            >> (False, None)
    """
    if string is None:
        return False, None
    if isinstance(string, (int, float)):
        return True, str(string)
    elif not isinstance(string, str):
        return False, None
    else:
      if string.isdigit():
          return True, string
      
      pattern = '^([+-]?\d+)([\.\,]\d+)$'
      match = re.match(pattern, string)
      if not match is None:
          int_part, dec_part = match.groups()
          return True, f'{int_part}.{dec_part[1:]}'
      else:
          return False, None
