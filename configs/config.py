import os 

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

config = {
    'app': {
        'config': {
            'name': 'full-stack-app'
        }
    },
    'llm': {
        'provider': 'openai',
        'config': {
            'model': 'gpt-3.5-turbo-0125',
            'temperature': 0.0,
            'max_tokens': 600,
            'top_p': 0.3,
            'stream': False,
            'prompt': (
                 """
                    You are a chatbot that uses given context to anwer to queries, if you can't answer with context reply - I cannot.

                Here are some guidelines to follow:

        1. You must only answer the question using the context.
        2. Refrain from explicitly mentioning the context provided in your response.
        3. The context should silently guide your answers without being directly acknowledged.
        4. If something is not found in the vector database, do not answer that and reply with a message such as 'i cannot'.
        5. Do not use phrases such as 'According to the context provided', 'Based on the context, ...' etc.
        6. Do not give talks on any of the religion, gender, racism, politics, or other sensitive topics. Maintain privacy and only answer questions found in the vector database.
        7. Ensure all responses are ethical, unbiased, and respectful.
        8. Avoid providing any medical, legal, or financial advice unless explicitly included in the context.
        9. Keep responses concise and to the point, ensuring clarity and relevance.
        10. Answer only using context within 80 words
        11.  Assume user is talking from indian POV, don't explicitly mention it
        12. You must answer using the context, if not reply - I cannot

    

        
        
       

                Context information:
                ----------------------
                $context
             

                ----------------------

                Query: $query
                Answer:
                    """ 
            ),
            'system_prompt': (
                "You are a chatbot that uses given context to answer to queries. if you can't answer using context, reply - I cannot"
            ),
            'api_key': "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",
         
        }
    },
   'vectordb': {
        'provider': 'pinecone',
        'config': {
            'metric': 'dotproduct',
            'vector_dimension': 1536,
            'index_name': PINECONE_INDEX_NAME,
            'serverless_config': {
                'cloud': 'aws',
                'region': 'us-east-1',
            },
            # 'hybrid_search': True,
        }
    },
    'embedder': {
        'provider': 'openai',
        'config': {
            'model': 'text-embedding-3-small',
            'api_key': "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"
        }
    },
  
}
