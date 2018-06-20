"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "sdsffffse",
            "answer": 4
        },
        {
            "input": "ddvvrwwwrggg",
            "answer": 3
        }
    ],
    "Extra": [
        {
            "input": "",
            "answer": 0
        },{
            "input": "abababaab",
            "answer": 2
        },{
            "input": "abababa",
            "answer": 1
        },{
            "input": "aa",
            "answer": 2
        },{
            "input": "a",
            "answer": 1
        }
    ]
}
