from currents.reliable_gen.tools.impl import google_search, reddit_search, sort

TOOL_GOOGLE_SEARCH = 'google_search'
TOOL_REDDIT_SEARCH = 'reddit_search'
TOOL_SORT = 'sort'

TOOLS = [
    {
        'type': 'function',
        'function': {
            'name': TOOL_GOOGLE_SEARCH,
            'description': 'use google search engine to search competitors for a given company',
            'parameters': {
                'type': 'object',
                'properties': {
                    'keyword': {
                        'type': 'string',
                        'description': 'the query keyword',
                    }
                },
                'required': ['keyword'],
                'additionalProperties': False
            },
            'strict': True
        }
    },
    {
        'type': 'function',
        'function': {
            'name': TOOL_REDDIT_SEARCH,
            'description': 'search competitors information from reddit posts and comments for a given company',
            'parameters': {
                'type': 'object',
                'properties': {
                    'query': {
                        'type': 'string',
                        'description': 'the query',
                    }
                },
                'required': ['query'],
                'additionalProperties': False
            },
            'strict': True
        }
    },
    {
        'type': 'function',
        'function': {
            'name': TOOL_SORT,
            'description': 'sort competitor list',
            'parameters': {
                'type': 'object',
                'properties': {
                    'competitors': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'the competitor list',
                    }
                },
                'required': ['competitors'],
                'additionalProperties': False
            },
            'strict': True
        }
    }
]

TOOL_MAP = {
    TOOL_REDDIT_SEARCH: reddit_search,
    TOOL_GOOGLE_SEARCH: google_search,
    TOOL_SORT: sort,
}
