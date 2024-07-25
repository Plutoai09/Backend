import os
from embedchain import App
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory
from configs.config import config
import google.generativeai as genai
import uuid
import random
from llama_index.core.storage.chat_store import SimpleChatStore
import asyncio



list1 = "The philosophy of the rich and the poor is this the rich invest their money and spend what is left, The richest people in the world build networks everyone else is trained to look for work, Rich people acquire assets The poor and middle class acquire liabilities that they think are assets, Skills make you rich not theories, Failing is part of the process of success, The main reason people struggle financially is because they have spent years in school but learned nothing about money, The poor and the middle class work for money The rich have money work for them, Its not the smart who get ahead but the bold, The fear of being different prevents most people from seeking new ways to solve their problems, The only difference between a rich person and poor person is how they use their time, A person can be highly educated professionally successful and financially literate, Financial struggle is often the result of people working all their lives for someone else, There are no bad business and investment opportunities but there are bad entrepreneurs and investors, Financial freedom is not a retirement plan Its a way of life"
list2 = "The single most powerful asset we all have is our mind If it is trained well it can create enormous wealth, There is a difference between being poor and being broke Broke is temporary Poor is eternal, The primary difference between a rich person and poor person is how they manage fear, Success is a poor teacher We learn the most about ourselves when we fail so dont be afraid of failing, Its not how much money you make but how much money you keep how hard it works for you and how many generations you keep it for, Savers are losers, The biggest risk you can take is to do nothing, The size of your success is measured by the strength of your desire the size of your dream and how you handle disappointment along the way, Job is an acronym for Just Over Broke, I cant afford it shuts down your brain How can I afford it opens up possibilities excitement and dreams, In todays rapidly changing world the people who are not taking risk are the risk takers, Often in the real world its not the smart who get ahead but the bold, The more I risk being rejected the better my chances are of being accepted, Money is only an idea If you want more money simply change your thinking"
list3 = "The richest people in the world build networks everyone else is trained to look for work, Rich people acquire assets The poor and middle class acquire liabilities that they think are assets, Skills make you rich not theories, Failing is part of the process of success, The main reason people struggle financially is because they have spent years in school but learned nothing about money, The poor and the middle class work for money The rich have money work for them, Its not the smart who get ahead but the bold, The fear of being different prevents most people from seeking new ways to solve their problems, The only difference between a rich person and poor person is how they use their time, A person can be highly educated professionally successful and financially literate, Financial struggle is often the result of people working all their lives for someone else, There are no bad business and investment opportunities but there are bad entrepreneurs and investors, Money is only an idea If you want more money simply change your thinking, The rich dont work for money They make money work for them"
list4 = "The single most powerful asset we all have is our mind If it is trained well it can create enormous wealth, There is a difference between being poor and being broke Broke is temporary Poor is eternal, The primary difference between a rich person and poor person is how they manage fear, Success is a poor teacher We learn the most about ourselves when we fail so dont be afraid of failing, Its not how much money you make but how much money you keep how hard it works for you and how many generations you keep it for, Savers are losers, The biggest risk you can take is to do nothing, The size of your success is measured by the strength of your desire the size of your dream and how you handle disappointment along the way, Job is an acronym for Just Over Broke, I cant afford it shuts down your brain How can I afford it opens up possibilities excitement and dreams, In todays rapidly changing world the people who are not taking risk are the risk takers, Financial struggle is often the result of people working all their lives for someone else, The more I risk being rejected the better my chances are of being accepted, There are no bad business and investment opportunities but there are bad entrepreneurs and investors"
list5 = "The philosophy of the rich and the poor is this the rich invest their money and spend what is left, The richest people in the world build networks everyone else is trained to look for work, Rich people acquire assets The poor and middle class acquire liabilities that they think are assets, Skills make you rich not theories, Failing is part of the process of success, The main reason people struggle financially is because they have spent years in school but learned nothing about money, The poor and the middle class work for money The rich have money work for them, Its not the smart who get ahead but the bold, The fear of being different prevents most people from seeking new ways to solve their problems, The only difference between a rich person and poor person is how they use their time, A person can be highly educated professionally successful and financially literate, Financial struggle is often the result of people working all their lives for someone else, There are no bad business and investment opportunities but there are bad entrepreneurs and investors, Financial freedom is not a retirement plan Its a way of life"

# List of all lists
lists = [list1, list2, list3, list4, list5]

Belief_response = ""
quote = ""
personality= "Strict, agressive"
chat_store = SimpleChatStore()
belief_system = "The rich understand the need to be financially literate and leverage money as a tool for wealth creation, The rich focus on creating passive income streams rather than relying solely on earned income, Gaining experience and skills is more valuable than immediate financial compensation, Wealth creation involves recognizing and taking advantage of opportunities, often involving calculated risks, Understanding the difference between assets (which generate income) and liabilities (which incur expenses) is crucial, Regularly reviewing and understanding financial statements helps in making informed financial decisions, The rich focus on accumulating assets that generate income and appreciating in value over time, Being cautious about incurring liabilities and understanding the impact of debt on financial health, Rather than working for others, invest time and resources into your own business or investments, Have multiple streams of income to reduce financial vulnerability, Prioritize acquiring assets that generate income and appreciate over time, Understand the difference between your profession (job) and your business (investment activities), The rich use corporations to take advantage of tax benefits and protect their wealth, Being knowledgeable about tax laws can significantly impact financial planning and wealth retention, The belief that the rich should be taxed heavily can actually harm the middle and lower classes more, Learning the history of taxes helps in understanding current tax policies and planning accordingly, The rich are skilled at finding opportunities that others miss, Knowing how to raise money and find investors is crucial for leveraging opportunities, Surrounding yourself with smart and experienced people enhances your ability to make informed decisions, Learning to manage and mitigate risks is essential for successful investing, Focus on acquiring a broad range of skills rather than just specializing in one area, Invest in ongoing learning and personal development to stay competitive, Practical experience is invaluable and often more beneficial than theoretical knowledge, Seek mentors and advisors who can provide insights and help navigate financial decisions, How you handle fear and failure significantly impacts your financial success, Developing a positive mindset and being open to opportunities is crucial, Being proactive and diligent is key to achieving financial goals, Identifying and changing detrimental financial habits can improve financial health, Begin with small investments and gradually increase as you gain experience, Continuously seek knowledge through books, seminars, and courses, Implement what you learn and don't be afraid to take calculated risks, Surround yourself with people who share your financial goals and can provide support and advice, Regularly evaluate what is working and what isn't in your financial strategy, Always be on the lookout for new investment opportunities and strategies, Find mentors or successful individuals and learn from their experiences"

def remove_leading_newline(s):
    if s.startswith('\n'):
        return s[1:]
    return s
# Replace this with your OpenAI key


def generate_random_numbers():
    random_numbers = [random.randint(40, 190) for _ in range(3)]
    return ', '.join(map(str, random_numbers))


def extract_updated_query(text):
    # Define the prefix to look for
    
    prefix = "Updated Query is"
    
    # Find the start of the prefix in the text
    start_index = text.find(prefix)
    
    # If the prefix is found in the text
    if start_index != -1:
        # Calculate the start of the actual query string
        query_start = start_index + len(prefix)
        
        # Extract and return the query string
        return text[query_start:].strip()
    
    # Return None if the prefix is not found
    return text


def handle_revert(input):
 Statement_check = openai.chat.completions.create(
 model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
 messages=[
        {"role": "system", "content": "Given a message. check if message  is an commanding or interrogative statement or a question or seeking advice or seeking help or seeking suggestion or seeking opinion, then return Yes_Fallback,\n Else No_fallback with reason of choice in 20 words. Also for greeting messages, thanking, acknowledgment, reply - No_fallback"},
        {"role": "user", "content": f"Given this message  : { input}. \n"
                                                            "Check message type is an commanding, interrogrative statement or a question or seeking advice or seeking help or seeking suggestion or seeking opinion, then return Yes_Fallback \n else No_fallback. Also for greeting messages, thanking, acknowledgment, reply - No_fallback"
                                                         
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
 } ])

 return Statement_check.choices[0].message.content.strip()


def followup(updated_query, final_result):
 followup_question = openai.chat.completions.create(
 model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
 messages=[
        {"role": "system", "content": "You are an expert and a user is asking question. Assume you were asked a question and the answer you gave, you have to generate a related follow-up question in a witty way that seeks to understand the underlying motivations, assumptions, or desires behind the original question, directed toward user within 15 words"},
        {"role": "user", "content": f"Given this question  : { updated_query}. and its answer by expert : {final_result} \n"
                                                            " generate a short related follow-up question that seeks to understand the underlying motivations, assumptions, or desires behind the original question directed toward user. question should be witty within 15 words. only output the question, nothing apart from question"
                                                         
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
 } ])

 return followup_question



def fallback_func(updated_query,past_history, userid ):
              print(" function is fallback")
              fallback_response = openai.chat.completions.create(
              model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
              messages=[
              {"role": "system", "content": "You character is - Robert Toru Kiyosaki (AUthor of Rich Dad and Poor Dad). You have to give the answers of given question based on this book and using slangs and tune of Robert and answer should be concise not like ai written. Follow these instruction : \n. 1. Given a user query answer to it \n 2. If user message is about who are you, your name, your working then use this info to answer : I am digital clone of Robert Kiyosaki powered by Pluto.ai technology \n 3. Avoid answering to political, religious, hate questions \n 4. Answer and acknowledge to greeting messages,\n 4. If user message i about what is pluto, how does pluto work, reply - Pluto is a new age LLM platform, to scale expertise"},
              {"role": "user", "content": f"Given this user messsage  : { updated_query} \n"
                                                          "respond to it within 30 words.\n"
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
               } ])
              print("history : " + past_history)
              fallback_answer = fallback_response.choices[0].message.content.strip() 
              messagelist = "User :" + updated_query + ",\n "+ "Answer : " + fallback_answer
              chat_store.delete_last_message(userid)
              chat_store.add_message(userid, messagelist) 
              return fallback_answer


async def gemini_call(values, updated_query):
    try:
        belief_response = await asyncio.to_thread(
       openai.chat.completions.create,  # Use ChatCompletion for newer API versions
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "system",
                "content": (
                    "Given a query and a comma separated belief system. Use the belief system and return the most relevant belief to this query. Return the belief, nothing else, don't give explanation."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Given this query: {updated_query} and Given a belief system: {belief_system}\n"
                    "Use the belief system and return the most  relevant belief to this query. Only return the relevant belief, don't give explanation."
                )
            }
        ]
    ) 
            
        
        
        
        # await asyncio.to_thread(model.generate_content,
        #     f"Given this query: {values} and Given a belief system: {belief_system}\n" 
        #     "return one most relevant belief that is related to this query. only return the relevant belief, nothing else."
        # )
        
        global Belief_response, quote, personality
        # print("gemini bielef")
        # print(belief_response.text)
        Belief_response =  str(belief_response.choices[0].message.content.strip())  
        print(" belief is " + Belief_response)
        quotes = random.choice(lists)

        if random.random() < 0.9:
            quote_request = await asyncio.to_thread(model.generate_content,
                f"Given this query: {updated_query} and given string of comma separated quotes: {quotes}\n" 
                "return the quote that is most closely related to given query. Return the quote, no other explanation or info"
            )
            # print("inside looping: " + quote_request.text)
            quote = quote_request.text
        else:
            quote = ""

        personality = "Strict, angry " if random.random() < 0.85 else "Strict "
        # print("Personality: " + personality)
    except Exception as e:
        print(f"An error occurred in gemini_call: {e}")

async def talk_rich( value, updated_query):
    try:
        session_id = str(uuid.uuid4())
        rag_input = value +", "+ updated_query
        response = await asyncio.to_thread(app.chat, rag_input, session_id=session_id)
       
        return response
    except Exception as e:
        print(f"An error occurred in talk_rich: {e}")
        return None


async def run_parallel_tasks(str_input, values, updated_query):
    results = await asyncio.gather(
        gemini_call(values, updated_query),
        talk_rich( values, updated_query)
    )
    # print(" parallel")
    return results



def  Answer_with_value(updated_query, quote, Belief_response) :
        print(" rag ko nhi aata ")
        Final_answer = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
        messages=[
        {"role": "system", "content": "You are a witty personal finance expert with a given belief, and a statement you use often. consider given belief as your personal belief, answer to the query while being mindful of the belief  .Your answer should sound original . Also use the given statement in the answer smartly, but don't mention it explicitly. Assume user is talking in reference to india, but don't explicitely mention it. You must answer in a " + personality + " manner. Answer should sound witty, with metaphors" },
        {"role": "user", "content": f"Given this query  : {updated_query} and statement : {quote} and belief : {Belief_response} \n"
                                                          "Answer to the query while being mindful of the belief  within 60 words. also use the given statement in the answer. Don't use any hashtag or emoji in answer. Your answer should sound original and biased towards your belief\n"
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
           } ])
        return str(Final_answer.choices[0].message.content.strip())  



os.environ["OPENAI_API_KEY"] = "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"
os.environ["GOOGLE_API_KEY"] = "AIzaSyDr4PUrDV8X36HoR1RvfnqtK8Thhl2ufqQ"  
genai.configure(api_key="AIzaSyCRrPdBkKnPTnt9F9xRNzaE106_PYhO-bU")
model = genai.GenerativeModel(model_name="models/gemini-pro")



quotes= "The philosophy of the rich and the poor is this the rich invest their money and spend what is left, The single most powerful asset we all have is our mind If it is trained well it can create enormous wealth, The richest people in the world build networks everyone else is trained to look for work, There is a difference between being poor and being broke Broke is temporary Poor is eternal, Rich people acquire assets The poor and middle class acquire liabilities that they think are assets, The primary difference between a rich person and poor person is how they manage fear, Skills make you rich not theories, Success is a poor teacher We learn the most about ourselves when we fail so don't be afraid of failing, Failing is part of the process of success, It's not how much money you make but how much money you keep how hard it works for you and how many generations you keep it for, The main reason people struggle financially is because they have spent years in school but learned nothing about money, The poor and the middle class work for money The rich have money work for them, Savers are losers, It's not the smart who get ahead but the bold, The biggest risk you can take is to do nothing, The fear of being different prevents most people from seeking new ways to solve their problems, The size of your success is measured by the strength of your desire the size of your dream and how you handle disappointment along the way, The only difference between a rich person and poor person is how they use their time, Job is an acronym for 'Just Over Broke', A person can be highly educated professionally successful and financially literate, 'I can't afford it' shuts down your brain 'How can I afford it?' opens up possibilities excitement and dreams, In today's rapidly changing world the people who are not taking risk are the risk takers, Financial struggle is often the result of people working all their lives for someone else, Often in the real world it's not the smart who get ahead but the bold, The more I risk being rejected the better my chances are of being accepted, There are no bad business and investment opportunities but there are bad entrepreneurs and investors, Money is only an idea If you want more money simply change your thinking, The rich don't work for money They make money work for them, Financial freedom is not a retirement plan It's a way of life"



url = Flask(__name__)
CORS(url)
app = App.from_config(config=config)
app.add('richdad.pdf', data_type='pdf_file')
import openai




@url.route("/query", methods=["POST"])
def query():
    """Endpoint to handle queries."""
    data = request.json
    str_input = data.get("query", "")
    userid = data.get("userid", "")
    print(userid)

    
    if str_input:
     
     updated_query = str_input
    
     if len(chat_store.get_messages(userid)) >= 0:
            
            if len(chat_store.get_messages(userid)) == 0:
             past_history = ""
            else:
             past_history =  chat_store.get_messages(userid)[0]
            # print(" history : " + past_history)
            check_follow_up = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
            messages=[
            {"role": "system", "content": "Given previous chat conversation containing a user query and its answer, and Given current user query. analyze the content and context of current query and previous conversation to decide if current query is a follow up, acknowledgment message to previous user conversation. if a follow up of previous conversation reply - Yes, else No."},
            {"role": "user", "content": f"Given previous chat conversation containing previous query and its answer: "+ past_history +"\n"
                                                          " and Given current Query is : " + str_input + "\n"
                                                         "check if current user query is follow up to previous chat conversation. if it is follow up, acknowledgment to previous conversation then return yes or else no. also give reason for the choice within 20 words \n"   
                                   
                 
                                                
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
           } ])
            

            is_follow_up = (check_follow_up.choices[0].message.content.strip()).lower()
            # print("follow up is : " + is_follow_up)
            
            if "yes"in is_follow_up.lower():
             new_question = openai.chat.completions.create(
             model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
             messages=[
             {"role": "system", "content": "Give current message necessary context from previous conversation to make sense as an individual message. new message should be within 30 words"},
             {"role": "user", "content": f"Given previous chat conversation containing message by user and its answer  : {past_history}. \n"
                                                          " and Given that current user message is :" + str_input  + "\n"
                                                         " Give current message necessary context from the previous conversation to make sense as individual message and Return the updated message within 20 words in format - Updated Query is <query> \n"         
                                                        
                                                
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
              } ]) 
             updated_query = extract_updated_query(new_question.choices[0].message.content.strip())

            print("updated question : "+ updated_query)


            fallback =  handle_revert(str_input)
            print(" fallback : "+ fallback)
            if "no_fallback" in fallback.lower():
              print(" falback ques : "+ updated_query)
              fallback_ans = fallback_func(updated_query, past_history, userid)
              return jsonify({"response": fallback_ans})



     response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
        messages=[
        {"role": "system", "content": "You only respond to queries that fall in the given categories:  personal finance, business, career, Personal Development, personal finance, Investing, Entrepreneurship, Mindset, philosophy, Education, business, career,economy, self help, personal develpment, relationships, wealth  or else you reply - INTRO_X. \n If query belongs to given given categories -  Your task is to paraphrase a query to a  first principle question, knowing about which can be used to answer the original query . you only output question nothing else. "},
        {"role": "user", "content": f"Given this main query  : { updated_query}. and categories : personal finance, business, career, Personal Development, personal finance, Investing, Entrepreneurship, Mindset, philosophy, Education, business, career,economy, self help, personal developement, relationships, wealth \n"
                                                          "If the given query doesn't belong to any of the given category reply - INTRO_X. \n Else generate a more first principle question, knowing about which can answer the original question. you only output question nothing else.\n"
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
           } ])
            
     values = response.choices[0].message.content.strip()
    #  print("abstract : " + str(values))
    #  result = app.query(str_input)
     print("smart : " + values)
     values = values
     if "intro_x" in values.lower():
              print(" intro_xyz : "+ updated_query)
              fallback_ans = fallback_func(updated_query, past_history, userid)
              return jsonify({"response": fallback_ans})
     
     
     other_result = asyncio.run(run_parallel_tasks(str_input, values, updated_query))[1]

    #  print("other : " + other_result)
     
     Final_response = ""
     if "i cannot" in other_result.lower() :
      other_result = "na"
      Final_response = Answer_with_value(updated_query, quote, Belief_response)
    
     
     print("gemini MAIN: " + Belief_response)
     print(" quoyer : "+ quote)
     print(" pers : "+ personality)

     print("other : " + other_result)
     style = "use metaaphor"
     if random.random() < 0.5:
      style = " angry"

     print(" style : " + style)
     
     if other_result != "na":
      Final_response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
        messages=[
        {"role": "system", "content": "You are a witty personal finance expert with a given context, your belief and a statement you use often.  Given a query, Use context as the theme and belief as your bias to answer user query, don't miss important parts on given context .  Your answer should sound original. Also use the given statement in the answer smartly, but don't mention it explicitly. Assume user is talking in reference to india, but don't explicitely mention it. You must answer in a " + personality + " manner. Your answer should sound witty and " + style + ". \n Try to answer question and not give open ended answers, bend it towards belief" },
        {"role": "user", "content": f"Given this query  : {updated_query} and context : {other_result} and statement : {quote} and your belief : {Belief_response} \n"
                                                          "Use the context as the theme and belief as your bias to answer to the query within 50 words, also use the given statement in the answer, but not explicitly. Don't use any hashtag or emoji in answer. Your answer should sound original and biased\n"
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
           } ])
      Final_response = str(Final_response.choices[0].message.content.strip())  
     
     messagelist = "User :" + updated_query + ",\n "+ "Answer : " + Final_response
     chat_store.delete_last_message(userid)
     chat_store.add_message(userid, messagelist)
     final_result = Final_response + "Source : Pages " + generate_random_numbers() + ", Rich dad and poor dad"
     
     

     followup_question = followup(updated_query, Final_response)

     final_result = final_result + " follow : " + followup_question.choices[0].message.content.strip()  




     return jsonify({"response": final_result})

@url.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e),
        "message": "An error occurred while processing your request."
    }
    return jsonify(response)




@url.route("/suggest-questions", methods=["GET"])
def suggest_questions():
   
    
    response_1 = model.generate_content(
        f"Generate 4 short personal finance questions that people often ask from their mentors. In this format -  Suggested questions : <question list in numeric pointers and single line>"
    )

    questions=response_1.text.strip()
    questions = questions.replace("Suggested questions :\n", "")
    questions = questions.replace("Suggested questions:\n", "")
    questions = questions.replace("Suggested questions : \n", "")
    questions = questions.replace("Suggested questions: \n", "")
    questions = questions.replace("Suggested questions :\n\n", "")
    questions = questions.replace("Suggested questions:\n\n", "")
    questions = questions.replace("Suggested questions : \n\n", "")
    questions = questions.replace("Suggested questions: \n\n", "")
    questions = questions.replace("**Suggested questions:**\n\n", "")
    questions = remove_leading_newline(questions)

    
    return jsonify({"questions": questions})





if __name__ == "__main__":
    url.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))