

import re

# before adding openAI or other LLM calls, we can use simple rule-based conversions

def nl_to_sql(question: str) -> str:
    """
    Convert a natural language question to a SQL query.
    args: question (str): The natural language question.
    returns: str: The corresponding SQL query.
    
    """
    q = question.lower()

    if "top 5 products" in q:
        return """
        SELECT p.name, SUM(s.quantity * s.prince) AS revenue
        FROM products p
        JOIN sales s ON p.id = s.product_id
        GROUP BY p.id
        ORDER BY revenue DESC
        LIMIT 5;

        """
    
    if "all products" in q:
        return "SELECT * FROM products;"
    
    return "SELECT 'Query not recognized';"