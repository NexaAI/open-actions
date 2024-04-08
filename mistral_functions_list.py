import functools
import mistral_functions_list
from actions.content_creator.college_board_api import get_institution

FUNCTION_LIST = {"get_institution": functools.partial(get_institution)}

TOOL_LIST = [
    {
        "type": "function",
        "function": {
            "name": "get_institution",
            "description": "Get school information from the College Scorecard.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the school to search for.",
                    },
                    "zip": {
                        "type": "string",
                        "description": "Postal code of the school.",
                    },
                    "city": {
                        "type": "string",
                        "description": "City of the school.",
                    },
                    "state": {
                        "type": "string",
                        "description": "State of the school.",
                    },
                },
                "required": ["name"],
            },
        },
    },
]
