from typing import Dict, List, Tuple

class HttpGenericValidator:

    @staticmethod
    def validate(required_fields: List[str], body: Dict) -> Tuple[bool, str]:
        missing_fields = []
        for field in required_fields:
            if field not in body:
                missing_fields.append(field)
        if(len(missing_fields) > 0):
            http_error = 'Missing required field (s): {}'.format(', '.join(missing_fields))
            return False, http_error
        return True, None
