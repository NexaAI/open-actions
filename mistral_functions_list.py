tools = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_answer_from_college_board",
            "description": "Get school information from the College Scorecard.",
            "parameters": {
                "type": "dict",
                "properties": {
                    "school_name": {
                        "type": "string",
                        "description": "The name of the school.",
                    },
                    "zip": {
                        "type": "string",
                        "description": "The postal code where the school is located.",
                    },
                    "city": {
                        "type": "string",
                        "description": "The city where the school is located.",
                    },
                    "state": {
                        "type": "string",
                        "description": "The state where the school is located.",
                    },
                    "locale": {
                        "type": "integer",
                        "description": "The locale of the school.",
                    },
                    "address": {
                        "type": "string",
                        "description": "The address of the school.",
                    },
                    "alias": {
                        "type": "string",
                        "description": "Any alias for the school.",
                    },
                    "dolflag": {
                        "type": "integer",
                        "description": "Department of Labor flag.",
                    },
                    "branches": {
                        "type": "integer",
                        "description": "The number of branches the school has.",
                    },
                    "men_only": {
                        "type": "integer",
                        "description": "Whether the school is men only.",
                    },
                    "operating": {
                        "type": "integer",
                        "description": "Whether the school is currently operating.",
                    },
                    "ownership": {
                        "type": "integer",
                        "description": "The ownership status of the school.",
                    },
                    "region_id": {
                        "type": "integer",
                        "description": "The region ID of the school.",
                    },
                    "accreditor": {
                        "type": "string",
                        "description": "The accrediting agency of the school.",
                    },
                    "school_url": {
                        "type": "string",
                        "description": "The URL of the school's website.",
                    },
                    "state_fips": {
                        "type": "integer",
                        "description": "The FIPS code for the state.",
                    },
                    "women_only": {
                        "type": "integer",
                        "description": "Whether the school is women only.",
                    },
                    "main_campus": {
                        "type": "integer",
                        "description": "Whether the location is the main campus.",
                    },
                    "online_only": {
                        "type": "integer",
                        "description": "Whether the school is online only.",
                    },
                    "endowment": {
                        "type": "dict",
                        "description": "The endowment of the school if any.",
                    },
                    "faculty_salary": {
                        "type": "integer",
                        "description": "Average faculty salary.",
                    },
                    "peps_ownership": {
                        "type": "string",
                        "description": "PEPS ownership status.",
                    },
                    "ft_faculty_rate": {
                        "type": "float",
                        "description": "Full-time faculty rate.",
                    },
                    "under_investigation": {
                        "type": "integer",
                        "description": "Whether the school is under investigation.",
                    },
                    "price_calculator_url": {
                        "type": "string",
                        "description": "URL for the tuition price calculator.",
                    },
                    "minority_serving": {
                        "type": "dict",
                        "description": "Indicates if the school is minority-serving.",
                    },
                    "title_iv": {
                        "type": "dict",
                        "description": "Title IV status and data.",
                    },
                    "degrees_awarded": {
                        "type": "dict",
                        "description": "Data on degrees awarded.",
                    },
                    "tuition_revenue_per_fte": {
                        "type": "integer",
                        "description": "Tuition revenue per full-time equivalent student.",
                    },
                    "instructional_expenditure_per_fte": {
                        "type": "integer",
                        "description": "Instructional expenditure per full-time equivalent student.",
                    },
                    "institutional_characteristics": {
                        "type": "dict",
                        "description": "Characteristics of the institution.",
                    },
                },
                "required": ["school_name"],
            },
        },
    },
]
