TOOL_LIST = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_answer_from_college_board",
            "description": "Get school information from the College Scorecard.",
            "parameters": {
                "type": "dict",
                "properties": {
                    "name": {
                        "type": "str",
                        "description": "The name of the school to search for.",
                    },
                },
                "required": ["name"],
            },
        },
    },
]
