prompt_template ="""
You are an expert at creating exam-style questions based on programming-related text.

Your task:
- ONLY generate questions.
- DO NOT provide any answers or explanations.
- DO NOT summarize or comment on the text.
- Return only a numbered list of meaningful and challenging questions.

TEXT:
------------
{text}
------------

QUESTIONS:
"""



refine_template = ("""
You are an expert at creating practice questions based on coding material and documentation.
Your goal is to help a coder or programmer prepare for a coding test.
We have received some practice questions to a certain extent: {existing_answer}.
We have the option to refine the existing questions or add new ones.
(only if necessary) with some more context below.
------------
{text}
------------

Given the new context, refine the original questions in English.
If the context is not helpful, please provide the original questions.
QUESTIONS:
"""
)