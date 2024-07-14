# import os
# from flask_cors import CORS
# from flask import Flask, request, jsonify
# from llama_index.embeddings.gemini import GeminiEmbedding
# from llama_index.llms.gemini import Gemini
# from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
# from llama_index.core.node_parser import SentenceSplitter
# from llama_index.core.storage.chat_store import SimpleChatStore
# from llama_index.core.memory import ChatMemoryBuffer
# from llama_index.core.evaluation import FaithfulnessEvaluator
# import google.generativeai as genai
# import openai


# # Set your OpenAI API key
# openai.api_key = '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'



# app = Flask(__name__)
# CORS(app)
# # Initialize the model and settings
# model = genai.GenerativeModel(model_name="models/gemini-pro")
# os.environ["GOOGLE_API_KEY"] = "AIzaSyDr4PUrDV8X36HoR1RvfnqtK8Thhl2ufqQ"
# gemini_embedding_model = GeminiEmbedding(model_name="models/embedding-001")
# llm = Gemini(model_name="models/gemini-pro", temperature= 0)
# Settings.llm = llm
# Settings.embed_model = gemini_embedding_model
# Settings.node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=20)
# Settings.num_output = 256
# Settings.context_window = 32000
# Persist_dir = "./storage"

# # Initialize or load the index
# if not os.path.exists(Persist_dir):
#     documents = SimpleDirectoryReader("doc").load_data()
#     index = VectorStoreIndex.from_documents(documents)
#     index.storage_context.persist(persist_dir=Persist_dir)

# else:
#     storage_context = StorageContext.from_defaults(persist_dir=Persist_dir)
#     index = load_index_from_storage(storage_context=storage_context)



# #-------------------------------------------------------------------------------------
# def extract_updated_query(text):
#     # Define the prefix to look for
#     print("text: " + text )
#     prefix = "Updated Query is"

#     # Find the start of the prefix in the text
#     start_index = text.find(prefix)

#     # If the prefix is found in the text
#     if start_index != -1:
#         # Calculate the start of the actual query string
#         query_start = start_index + len(prefix)

#         # Extract and return the query string
#         return text[query_start:].strip()

#     # Return None if the prefix is not found
#     return text

# #----------------------------------------------------------------

# def check_string(input_string):
#     # Convert the string to lowercase for case-insensitive comparison
#     lower_string = input_string.lower()

#     # Check if either of the phrases is present
#     if 'the provided context' in lower_string or 'i cannot' in lower_string or 'i am an expert q&a' in lower_string or 'question cannot be answered' in lower_string or 'the context does not mention' in lower_string:
#         return 'no'
#     else:
#         return input_string



# #------------------------------------------------------------------------------------------

# def find_key_value_pair(string1, string2):
#     # Parse the key-value pairs from string1
#   #  string1_lower = string1.lower()
#     string2_lower = string2.lower()

#     pairs = [pair.split(": ") for pair in string1.split(", ")]


#     # Check if any key is present in string2
#     for key, value in pairs:
#         if key.lower() in string2_lower:
#             print("g : " + value)
#             return f"You can purchase it from here: {value}"

#     return "no"
# #--------------------------------------------------------------------------------------------


# def check_six_words_in_string(stringa, stringb):
#     # Split stringa into words
#     words_a = stringa.split()

#     # Generate all 6-word sequences from stringa
#     six_word_sequences = [" ".join(words_a[i:i+6]) for i in range(len(words_a) - 5)]

#     # Check if any of the 6-word sequences are present in stringb
#     for seq in six_word_sequences:
#         if seq in stringb:
#             return "Can you be more clear?"

#     # If no sequence is found, return stringb as it is
#     return stringb
# #-----------------------------------------------------------------------------------------------






# query_engine = index.as_query_engine()
# chat_store = SimpleChatStore()

# @app.route("/query", methods=["POST"])
# def query():
#     """Endpoint to handle queries."""
#     data = request.json
#     str_input = data.get("query", "")
#     userid = data.get("userid", "default_user")

#     if str_input:
#         # memory = ChatMemoryBuffer.from_defaults(
#         #     token_limit=8000,
#         #     chat_store=chat_store,
#         #     chat_store_key=userid,
#         # )

#     #affiliate links
#         Gadgets = " OnePlus Buds Z3: https://amzn.in/d/6B1PBMy, Sony TWS WF-1000XM5: https://amzn.in/d/557hst5, Panasonic New 2024 EU Series AC:  https://amzn.in/d/fHD5sbn, itel s24: https://www.itel-india.com/product/s24/ , IMO Z7: https://amzn.in/d/238N4gZ , IQOO Z9X: https://www.iqoo.com/in/products/param/z9x_5g , Oneplus go tablet: https://www.oneplus.in/buy-oneplus-pad-go , Lava Pro smartwatch: https://shop.lavamobiles.com/products/prowatch-zn?variant=48783023800630 , OnePlus Nord CE4: https://amzn.in/d/acE6zdn , Redmi Note 13 Pro: https://amzn.in/d/iVNfkrq , Poco X6 Pro: https://amzn.in/d/i1xzdKa , OnePlus Nord 3 5G: https://amzn.in/d/i1xzdKa , Honor 90: https://amzn.in/d/cndn5L8 , Nothing Phone 2A: https://amzn.in/d/2qPZu1g , Sonos Beam 2 soundbar: https://amzn.in/d/2VLQzti , Logitech webcam 4K: https://amzn.in/d/4ntP1FJ"

#         personality = "I am a digital clone of Abhishek Bhatnagar, powered by Gemini, LLaMA, and Pluto.ai proprietary technology. Abhishek is the founder and editor-in-chief of the tech website and media publication Gadgets To Use."

#         #Source = " OnePlus Buds Z3: https://amzn.in/d/6B1PBMy, Sony TWS WF-1000XM5: https://amzn.in/d/557hst5, Panasonic New 2024 EU Series AC:  https://amzn.in/d/fHD5sbn, itel s24: https://www.itel-india.com/product/s24/ , IMO Z7: https://amzn.in/d/238N4gZ , IQOO Z9X: https://www.iqoo.com/in/products/param/z9x_5g , Oneplus go tablet: https://www.oneplus.in/buy-oneplus-pad-go , Lava Pro smartwatch: https://shop.lavamobiles.com/products/prowatch-zn?variant=48783023800630 , OnePlus Nord CE4: https://amzn.in/d/acE6zdn , Redmi Note 13 Pro: https://amzn.in/d/iVNfkrq , Poco X6 Pro: https://amzn.in/d/i1xzdKa , OnePlus Nord 3 5G: https://amzn.in/d/i1xzdKa , Honor 90: https://amzn.in/d/cndn5L8 , Nothing Phone 2A: https://amzn.in/d/2qPZu1g , Sonos Beam 2 soundbar: https://amzn.in/d/2VLQzti , Logitech webcam 4K: https://amzn.in/d/4ntP1FJ"
#       #source link
#         Source = "Exploring the virtual world on slowroads.io: www.slowroads.io, Panasonic New 2024 EU Series AC review: www.panasonicnewacreview.com, Saving expired Google Pay vouchers using apps: www.googlepayvouchers.com, Itel S24 smartphone features and review: www.itels24.com, IMO Z7 smartwatch phone for child safety: www.imoz7.com, IQOO Z9X budget phone overview: www.iqooz9x.com, Reality check on No Cost EMI: www.nocostemi.com, Monitoring battery health for Android users: www.batteryhealthmonitor.com, Avoiding AI detection in academic writing: www.aiacademicwriting.com, Finding Wi-Fi passwords using Instabridge app: www.instabridgewifi.com, Improving TV performance by enabling Apps Only mode: www.tvappsonly.com, Eliminating grammar mistakes in emails with Quillbot extension: www.quillbotemails.com, Checking deleted WhatsApp messages through notification history: www.whatsappdeletedmessages.com, Improving 5G connectivity issues with NetMonster app: www.netmonsterapp.com, Hidden Instagram feature to start a game with emojis: www.instagramemojigame.com, Using phone as a Bluetooth speaker with AudioRelay app: www.audiorelayapp.com, Free YouTube Premium experience with Brave Browser: www.bravebrowserpremium.com, Resizing photos efficiently using Squoosh.app: www.squooshphotos.com, Free Microsoft Office alternative with OnlyOffice: www.onlyofficealternative.com, Sonos Beam 2 soundbar review: www.sonosbeam2.com, Discovering Aptoide, the secret app store: www.aptoideappstore.com, Lava Pro smartwatch overview: www.lavaprowatch.com, OnePlus Nord CE4 phone review: www.oneplusnordce4.com, Free Adobe podcast tool for audio clean-up: www.adobepodcasttool.com, Installing essential software easily with Ninite.com: www.ninitesoftware.com, Top 5 phones under 20,000 rupees: www.top5phonesunder20000.com, Creating custom video stickers on Instagram: www.instagramvideostickers.com, Top 5 phones under 30,000 rupees: www.top5phonesunder30000.com, Using call bomber service for persistent calling: www.callbomberservice.com, Logitech 4K webcam for enhanced video calls: www.logitech4kwebcam.com, Enhanced mobile productivity with PicsArt app: www.picsartmobile.com, Translating videos across languages with Rask.ai: www.raskvideotranslation.com, Anonymous global communication with Walkie Talkie app: www.walkietalkieglobal.com, Wearpods smartwatch with integrated TWS earphones: www.wearpodswatch.com, Tracking someone's location with Google Maps: www.trackgooglemaps.com, Discovering 123Apps for free creator tools: www.123appscreatortools.com, Sennheiser Ascentum wireless headphones review: www.sennheiserascentum.com, Vivo V30 performance at Qutub Minar: www.vivov30performance.com, Honor Choice Watch review: www.honorchoicewatch.com, Free learning resources with Comidoc: www.comidoclearning.com, Transforming videos into anime style with ImageUpscaler AI tool: www.imageupscalervideos.com, OnePlus smartwatch features and comparison with Apple Watch: www.onepluswatchcomparison.com, OpenAI's SORA for creating cinematic videos from text: www.openaisoravideos.com, Improving website visibility with youstyle.ai: www.youstylewebsitevisibility.com, Infinix Hot 40i smartphone features and review: www.infinixhot40i.com, Affordable international data solution with Air Allo: www.airallo.com, Booking IRCTC retiring rooms for convenience at railway stations: www.irctcretiringroomsbooking.com, Reversing UPI transactions and getting refunds: www.upireversals.com, OnePlus Buds Z3 wireless earbuds review: www.oneplusbudsz3.com, Effective Mosquito and Fly Control Solutions for Your Office: www.officepestsolutions.com, Create Stunning Social Media Images with Remaker Face Swap: www.remakerfaceswap.com, OnePlus' Latest Smartphone Features and Specifications: www.onepluslatest.com, Upload High-Quality WhatsApp Status Videos Easily: www.whatsappvideos.com, Three-Way Multi-Plug for Simultaneous Device Charging: www.multiplugcharging.com, IRCTC Retiring Rooms for Comfortable Accommodations at Railway Stations: www.irctcretiringrooms.com, Read Deleted WhatsApp Messages and Statuses with WAMR: www.wamrapp.com, Create 4K Quality Videos Using Hyper.ai: www.hyperaivideos.com, Free Up Gmail Storage with Simple Steps: www.freeupgmailstorage.com, Plan Your Trip with tripplanner.ai: www.tripplanner.ai, Hidden Feature of Google Drive for Scanning Documents: www.hiddenfeaturegoogledrive.com, Google Maps Location Tracking Tips: www.mapstrackingtips.com, Summarize YouTube Videos with AI: www.summarizevideos.com, Xume Health Food Scanner App for Nutrition Info: www.xumefoodscanner.com, Improve Your Resume with Hireflow.net: www.hireflow.net, Access PlayStation Games on ACTDUCK GAMES App: www.actduckgames.com, Sell Clothes Easily with FreeUp App: www.freeupclothes.com, Check Amazon Reviews with Reviewmeta: www.reviewmetareviews.com, Take Free Online Courses on Class Central: www.classcentralcourses.com, ChatGPT 4 Features on wrtn.ai: www.chatgpt4wrtn.ai, Apply for NCGG Internship Opportunities: www.ncgginternships.com, Summarize Articles with ChatGPT Summarization Trick: www.chatgptsummarize.com, Guide City App for Travel Information: www.guidecitytravel.com, Remote Phone Management with Plain App: www.plainremotephone.com, Add Music to Instagram Profile Easily: www.instagrammusicadd.com, Touch the Notch App for Custom Phone Controls: www.touchnotchapp.com, Delhi T3 Terminal Water Bottle Pricing Tips: www.delhiwaterbottle.com, Enhance Earphone Sound with Bass Booster and Equalizer App: www.bassboosterapp.com, Find Broadband Options with Sancharsaath.gov.in: www.sancharsaathbroadband.com, Create Shots from Videos with app.2short.ai: www.app2shortvideos.com, Enable iPhone Privacy Features: www.iphoneprivacyfeatures.com, Download 8K YouTube Videos with YTDLnis App: www.ytdlnisapp.com, Change Photo Backgrounds Easily: www.photobackgroundchanger.com, Get Free Credit Cards for Trials with DNSChecker: www.dnscheckercreditcards.com, Convert Videos to Lo-fi with Lofi Converter GUI Web App: www.loficonvertergui.com, Hide Lock Screen Chat Easily: www.hidelockscreenchat.com, Voice Cloning with Play.ht: www.playhtvoicecloning.com, Get Free Numbers and Temporary Emails with smsnator.online: www.smsnatorfree.com, Improve Photos with AI Photo Improver on Telegram: www.telegramphotoimprover.com, Portable DJ Setup Features: www.portabledjsetup.com, Transform Your Voice with Voice Changer App: www.voicechangerapp.com, Poco X6 Pro Features and Specifications: www.pocox6pro.com, Automatically Add Subtitles to Videos with Submagic.co: www.submagicvideos.com, Shorten YouTube Videos with Wizard.ai: www.wizardaivideos.com, Enhanced Privacy for Instagram DMs: www.instagramdmprivacy.com, Enhance Google Search with SGE at lab.google.com: www.googlesearchenhance.com, Vivo X100 Features and Specifications: www.vivox100.com, Create Deepfake Videos at fal.ai/camera: www.deepfakevideos.com, Windows 11 Co-Pilot AI Features: www.windows11copilot.com, Zebronics Astra 10 Features: www.zebronicsastra10.com, WhatsApp Lock Chat Feature: www.whatsapplockchat.com, AI Language Translation with Caption AI: www.captionailanguagetranslation.com, Unlimited Cloud Storage with Unlim App: www.unlimcloudstorage.com, Bold's Crown R Premium Smartwatch Features: www.boldcrownrsmartwatch.com, Lava Blaze 2 5G Features and Specifications: www.lavablaze25g.com, OnePlus Go Tablet Features and Specifications: https://www.instagram.com/reel/CydzOOAIqW-/?igsh=MXVuOWRrM3h1YnlqOA==, OnePlus Open Folding Phone Features and Specifications: https://www.instagram.com/reel/CydzOOAIqW-/?igsh=MXVuOWRrM3h1YnlqOA==, Sony WF-1000XM5 Headphones Features: www.sonywf1000xm5.com, Honor 90 Smartphone Features and Specifications: www.honor90.com, AI-Powered Paragraph App for Easy Replies: www.aiparagraphapp.com, itel S23 Plus Features and Specifications: www.itels23plus.com"




#        # response = chat_engine.chat(str_input)
#         messagelist ="no"
#         input = str_input
#         response = ""
#         updated_query = input




#         #if empty list
#         if len(chat_store.get_messages(userid))==0:
#            print("hello")
#            response = query_engine.query(f"Given this query: {input} ." +"and answer it within 25 words")
#         else:
#             print("input is : "+ input)
#             response = openai.chat.completions.create(
#             model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
#             messages=[
#             {"role": "system", "content": "You are  a chat bot which refine user query only if the subject of query is not clear and it doesn't make sense as an individual message"},
#             {"role": "user", "content": f"Given previous chat history of question asked by user and its answer by the system  : { chat_store.get_messages(userid)[0]}. \n"
#                                                           " and Given that new user Query is :" + input  + "\n"
#                                                          "Only If the subject of query is not clear then use the chat history's answer to add the necessary subject information to the query concisely. and Return the updated query in format - Updated Query is <query> \n"
#                                                           "else If the query is clear and not related to previous chat, return the query without any changes.\n"

#                                                                                 #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
#            } ])

#             updated_query = extract_updated_query(response.choices[0].message.content.strip())
#             print ("updated query : " + updated_query)
#      #       print("chat history : " + chat_store.get_messages(userid)[0])
#       #      print("message : " +  response.choices[0].message.content.strip())
#             response = query_engine.query(f"Given this query: {updated_query} ." +"and answer it within 25 words")
#         messagelist = "question :" + str_input + ", answer : " + str(response)


#         result = check_string(str(response))

#         # chat management
#         chat_store.delete_last_message(userid)
#         chat_store.add_message(userid, messagelist)


#         print("result : " + result)
#         if check_string(response.response) != "no":
#         #  print('inside')
#           source_link = model.generate_content(f"Given this query: {updated_query}. and \n " + "given string of key value pairs of topics with their respective links: " + Source + "\n" + "check if any topic is related to the query and if found return its respective link in the format - Source : <Link>. else return - NO")
#           if source_link.text != "NO" :
#              result = result + " " + source_link.text


#        # if(link_check.text != "SKIP"):
#         #    result = result + "\n" + link_check.text

#         affiliate = find_key_value_pair(Gadgets, updated_query)
#         if affiliate != "no" :
#             result = result + "\n" + affiliate
#             print("link: "+affiliate)



#         new_string = ""


#         if check_string(response.response) == "no":
#          new_string = "no"
#         else:
#          for char in response.response.lower():
#             if char.isalpha():
#                 new_string += char

#       #  print("condition : " + new_string + "\n")

#         if new_string == "no":
#             # gemini_response = model.generate_content(
#             #     f" if this: {str_input}, is about either about tech review or tech suggestions or tech tips & tricks then answer - Reach out at Zaidjunaid3 else if it is a tech related question then answer as usual else if it is not a tech related question then answer: Lets stick to tech."
#             # )
#             sample_response = model.generate_content(
#                 f"Given the query: {str_input} \n. Check the following five criterias to respond without naming the criterias : \n 1. If the query is a greeting message like - Hi, Hey, hello, whats up, how are you etc. reply in this theme - Hey lets deep dive into technology. \n  2. Else If the query is about who you are, your name etc. answer using this info in few words: {personality} \n 3. else If the query is related to politics, voilence, religion, gender, abuse, Legal Matters, personal matters, relationship, or any other non technology related query reply in this theme : Buddy, Lets stick to Technical topics only! \n 4. Else If the query is about Specific Gadgets information, suggestion, reviews, tips or trick, reply in this theme - Would love to discuss this in detail, you can reach out to me at gadgetstouse@gmail.com.  \n 5. Else Answer to query in 30 words "
#             )

#             print("loop")
#             welcome_reply = " Hey lets deep dive into technology."
#             suggestion_reply = "Would love to discuss this in detail, you can reach out to me at gadgetstouse@gmail.com. "
#             outlier = "Buddy, Lets stick to Technical topics only!"
#             result

#             if sample_response.text in welcome_reply or sample_response.text in suggestion_reply or sample_response.text in outlier:
#              result = sample_response.text
#             else:
#              verify_string = "Check the following five criterias to respond without naming the criterias : \n 1. If the query is a greeting message in theme of  - Hi, hello, whats up, how are you etc. Answer to query using iteration of this - Hey lets deep dive into technology. \n  2. Else If the query is about who you are, your name etc. answer using this info in few words: {personality} \n 3. else If the query is related to politics, voilence, religion, gender, abuse, Legal Matters, personal matters, relationship, or any other non technology related query, answer using this theme : Buddy, Lets stick to Technical topics only! \n 4. Else If the query is about Specific Gadgets information, suggestion, reviews, tips or trick, answer to query using this theme - Would love to discuss this in detail, you can reach out to me at gadgetstouse@gmail.com.  \n 5. Else Answer to query in 30 words"
#              result = check_six_words_in_string(verify_string, sample_response.text)

#         return jsonify({"response": result})

#     return jsonify({"response": "No input provided"}), 400

# # @app.route("/suggest-questions", methods=["GET"])
# # # def suggest_questions():
# # #     {
# # #     "text": "The OnePlus Go tablet stands out with its 2K display that offers vibrant colors and clarity, paired with a responsive 90Hz refresh rate. It includes features like a 4G SIM card slot for calls and Wi-Fi hotspot creation, quad speakers with Dolby Atmos support, and a sleek, lightweight metal casing. Priced affordably at 20,000 rupees, it's ideal for gaming and multimedia entertainment.\n\nThe OnePlus Open is a new folding phone with a stainless steel frame, metal unibody design, and leather back. It functions both as a phone and a tablet, featuring displays with high refresh rates on both sides. It introduces multitasking capabilities with a taskbar, allowing for seamless file attachments in emails and simultaneous use of up to three applications or two games. Equipped with five cameras including a periscope zoom lens, Snapdragon 8 Gen 2 processor, 16GB RAM, and 512GB storage, it also boasts fast charging capabilities and IPX4 certification.\n\nSony's TWS WF-1000XM5 headphones offer compact, lightweight design with excellent sound quality and comfortable memory foam tips. They are IPX4 certified for water resistance and feature a smart equalizer for customizable audio preferences, along with spatial audio for immersive surround sound. Smart active noise cancellation adjusts automatically to ambient mode during conversations, and they support 24 hours of music playback with wireless charging. Available in various colors, these headphones provide premium features in eco-friendly packaging.\n\nThe Honor 90 smartphone impresses with a 200-megapixel camera and Snapdragon 7 Gen 1 processor, delivering top-notch photography and gaming performance. It boasts a seamless display and supports fast charging with a 5000 mAh battery, though the charger needs to be purchased separately. Offering unique features at its price point, it stands out in the market.\n\nThe AI-powered Paragraph AI app enhances productivity by assisting in composing responses to English chats or emails. Available on Android and iOS, this app integrates with your keyboard to facilitate easy drafting and editing of replies based on context and mood.\n\nThe itel S23 Plus features a premium design with dual curved displays and includes NFC for contactless payments. It offers WhatsApp call recording and comes with a 2-year warranty. Purchasing from Amazon includes free earbuds and a 100-day screen replacement guarantee. Priced at ₹14,000, it packs 8GB RAM, 256GB storage, and an 18W fast charger. Security features like Thrift Alert deter theft during charging, while App Lock and Dual App functionalities enhance privacy. The phone boasts a 6.7-inch AMOLED display for vivid visuals.\n\nGmail's \"confidential mode\" allows users to send emails that automatically delete after a set time, enhancing security. Available on mobile apps and PCs, this feature lets senders set an expiry date and optionally add a password, preventing unauthorized access. Emails in confidential mode cannot be forwarded, copied, printed, or downloaded, ideal for sharing sensitive information securely.\n\nThe iPhone 15 Pro introduces a titanium frame for lighter yet robust construction, replacing stainless steel. It adopts USB-C compatibility like Android phones, though the charger is not included. Users receive a braided cable matching the phone's color scheme, enhancing both functionality and aesthetics in the Pro series.\n\nUrban's Titanium smartwatch combines premium aesthetics with functionality. Featuring a large, bright touchscreen and IP67 certification, it offers continuous heart rate, SPO2, and stress monitoring, along with body temperature tracking. Users enjoy customizable watch faces, Bluetooth calling, and a magnetic charger, all complemented by a 3-4 day battery life. The watch's luxury design and versatile features make it a standout in its category."
# # # }
# #     data = request.json
# #     text = data.get("text", "")
# #     if text:
# #         response_1 = model.generate_content(
# #             f"Generate  five suggested questions from the following text: {text}"
# #         )
# #         questions = response_1.text.strip()
# #         return jsonify({"questions": questions})
# #     return jsonify({"response": "No text provided"}), 400


# @app.route("/suggest-questions", methods=["GET"])
# def suggest_questions():
#     static_text = """
#   The OnePlus Go tablet stands out with its 2K display that offers vibrant colors and clarity, paired with a responsive 90Hz refresh rate. It includes features like a 4G SIM card slot for calls and Wi-Fi hotspot creation, quad speakers with Dolby Atmos support, and a sleek, lightweight metal casing. Priced affordably at 20,000 rupees, it's ideal for gaming and multimedia entertainment.\n\nThe OnePlus Open is a new folding phone with a stainless steel frame, metal unibody design, and leather back. It functions both as a phone and a tablet, featuring displays with high refresh rates on both sides. It introduces multitasking capabilities with a taskbar, allowing for seamless file attachments in emails and simultaneous use of up to three applications or two games. Equipped with five cameras including a periscope zoom lens, Snapdragon 8 Gen 2 processor, 16GB RAM, and 512GB storage, it also boasts fast charging capabilities and IPX4 certification.\n\nSony's TWS WF-1000XM5 headphones offer compact, lightweight design with excellent sound quality and comfortable memory foam tips. They are IPX4 certified for water resistance and feature a smart equalizer for customizable audio preferences, along with spatial audio for immersive surround sound. Smart active noise cancellation adjusts automatically to ambient mode during conversations, and they support 24 hours of music playback with wireless charging. Available in various colors, these headphones provide premium features in eco-friendly packaging.\n\nThe Honor 90 smartphone impresses with a 200-megapixel camera and Snapdragon 7 Gen 1 processor, delivering top-notch photography and gaming performance. It boasts a seamless display and supports fast charging with a 5000 mAh battery, though the charger needs to be purchased separately. Offering unique features at its price point, it stands out in the market.\n\nThe AI-powered Paragraph AI app enhances productivity by assisting in composing responses to English chats or emails. Available on Android and iOS, this app integrates with your keyboard to facilitate easy drafting and editing of replies based on context and mood.\n\nThe itel S23 Plus features a premium design with dual curved displays and includes NFC for contactless payments. It offers WhatsApp call recording and comes with a 2-year warranty. Purchasing from Amazon includes free earbuds and a 100-day screen replacement guarantee. Priced at ₹14,000, it packs 8GB RAM, 256GB storage, and an 18W fast charger. Security features like Thrift Alert deter theft during charging, while App Lock and Dual App functionalities enhance privacy. The phone boasts a 6.7-inch AMOLED display for vivid visuals.\n\nGmail's \"confidential mode\" allows users to send emails that automatically delete after a set time, enhancing security. Available on mobile apps and PCs, this feature lets senders set an expiry date and optionally add a password, preventing unauthorized access. Emails in confidential mode cannot be forwarded, copied, printed, or downloaded, ideal for sharing sensitive information securely.\n\nThe iPhone 15 Pro introduces a titanium frame for lighter yet robust construction, replacing stainless steel. It adopts USB-C compatibility like Android phones, though the charger is not included. Users receive a braided cable matching the phone's color scheme, enhancing both functionality and aesthetics in the Pro series.\n\nUrban's Titanium smartwatch combines premium aesthetics with functionality. Featuring a large, bright touchscreen and IP67 certification, it offers continuous heart rate, SPO2, and stress monitoring, along with body temperature tracking. Users enjoy customizable watch faces, Bluetooth calling, and a magnetic charger, all complemented by a 3-4 day battery life. The watch's luxury design and versatile features make it a standout in its category.
#     """
    
#     response_1 = model.generate_content(
#         f"Generate five suggested questions from the following text: {static_text}"
#     )
#     questions = response_1.text.strip()
#     return jsonify({"questions": questions})

# # Error handling in case something goes wrong
# @app.errorhandler(Exception)
# def handle_exception(e):
#     response = {
#         "error": str(e),
#         "message": "An error occurred while processing your request."
#     }
#     return jsonify(response), 500


# @app.route("/save", methods=["POST"])
# def save_to_system():
  
#     data = request.json
#     save_info = data.get("user_query", "")
#     save_text_to_file(save_info, "save.txt")

#     return jsonify("success"), 500



# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))




import os
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory,abort
import json
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.evaluation import FaithfulnessEvaluator
import google.generativeai as genai
import openai
import random 

from resources.resources import resources
from questions import ques


# Set your OpenAI API key
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")



app = Flask(__name__)
CORS(app)
# Initialize the model and settings
model = genai.GenerativeModel(model_name="models/gemini-pro")
gemini_embedding_model = GeminiEmbedding(model_name="models/embedding-001")
llm = Gemini(model_name="models/gemini-pro", temperature= 0.8)
Settings.llm = llm
Settings.embed_model = gemini_embedding_model
Settings.node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=50)
Settings.num_output = 256
Settings.context_window = 32000
Persist_dir = "./storage"

# Initialize or load the index
if not os.path.exists(Persist_dir):
    documents = SimpleDirectoryReader("doc").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=Persist_dir)
  
else:
    storage_context = StorageContext.from_defaults(persist_dir=Persist_dir)
    index = load_index_from_storage(storage_context=storage_context)



#-------------------------------------------------------------------------------------
def extract_updated_query(text):
    # Define the prefix to look for
    print("text: " + text )
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

#----------------------------------------------------------------

def check_string(input_string):
    # Convert the string to lowercase for case-insensitive comparison
    lower_string = input_string.lower()
    
    # Check if either of the phrases is present
    if 'the provided context' in lower_string or 'i cannot' in lower_string or 'i am an expert q&a' in lower_string or 'question cannot be answered' in lower_string or 'the context does not mention' in lower_string:
        return 'no'
    else:
        return input_string



#------------------------------------------------------------------------------------------

def find_key_value_pair(string1, string2):
    # Parse the key-value pairs from string1
  #  string1_lower = string1.lower()
    string2_lower = string2.lower()
 
    pairs = [pair.split(": ") for pair in string1.split(", ")]

    
    # Check if any key is present in string2
    for key, value in pairs:
        if key.lower() in string2_lower:
            print("g : " + value)
            return f"You can purchase it from here: {value}"

    return "no"
#--------------------------------------------------------------------------------------------


def check_six_words_in_string(stringa, stringb):
    # Split stringa into words
    words_a = stringa.split()
    
    # Generate all 6-word sequences from stringa
    six_word_sequences = [" ".join(words_a[i:i+6]) for i in range(len(words_a) - 5)]
    
    # Check if any of the 6-word sequences are present in stringb
    for seq in six_word_sequences:
        if seq in stringb:
            return "Can you be more clear?"
    
    # If no sequence is found, return stringb as it is
    return stringb
#-----------------------------------------------------------------------------------------------

def save_text_to_file(text, filename):
    with open(filename, 'a') as file:
        file.write(text + "\n")  
# Example usage:

#----------------------------------------------------------

def remove_leading_newline(s):
    if s.startswith('\n'):
        return s[1:]
    return s
#-----------------------------------------------------------------



query_engine = index.as_query_engine()
chat_store = SimpleChatStore()





# Endpoint to get all resources
@app.route('/load', methods=["GET"])
def load_data():
 return jsonify(resources)


# Endpoint to get a single resource by id
@app.route('/loads/<int:load_id>', methods=['GET'])
def get_resource(load_id):
    resource = next((r for r in resources if r['id'] == load_id), None)
    if resource is None:
        abort(404)
    return jsonify(resource)

# Endpoint to create a new resource
@app.route('/loads', methods=['POST'])
def create_resource():
    new_resource = request.get_json()
    new_resource['id'] = max(r['id'] for r in resources) + 1
    resources.append(new_resource)
    return jsonify(new_resource), 201

# Endpoint to update an existing resource by id
@app.route('/loads/<int:load_id>', methods=['PUT'])
def update_resource(load_id):
    updated_data = request.get_json()
    resource = next((r for r in resources if r['id'] == load_id), None)
    if resource is None:
        abort(404)
    resource.update(updated_data)
    return jsonify(resource)

# Endpoint to delete a resource by id
@app.route('/loads/<int:load_id>', methods=['DELETE'])
def delete_resource(load_id):
    global resources
    resources = [r for r in resources if r['id'] != load_id]
    return '', 204



# Endpoint to save the images into the static folder
@app.route('/imagesaver', methods=['POST'])
def save_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file.save(os.path.join('static/images', file.filename))
        return jsonify({'message': 'File uploaded successfully'}), 201

    return jsonify({'error': 'Invalid file'}), 400


# Endpoint to save the transcript
@app.route('/transcriptSave', methods=['POST'])
def save_transcript():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text_to_append = data['text']

    try:
        with open('doc/Transcript.txt', 'a') as file:
            file.write(text_to_append + '\n')
        
        return jsonify({"message": "Text appended successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

@app.route("/questiontest",methods=['GET'])
def load_question():
    return jsonify(ques)

@app.route("/questiontest/<int:question_id>",methods=['GET'])
def get_question(question_id):
    question = next((q for q in ques if q['id'] == question_id), None)
    if question is None:
        abort(404)
    return jsonify(question)

@app.route("/questiontest",methods=['POST'])
def create_question():
    new_question = request.get_json()
    new_question['id'] = max(q['id'] for q in ques) + 1
    ques.append(new_question)
    return jsonify(new_question), 201

@app.route("/questiontest/<int:question_id>",methods=['PUT'])
def update_question(question_id):
    updated_data = request.get_json()
    question = next((q for q in ques if q['id'] == question_id), None)
    if question is None:
        abort(404)
    question.update(updated_data)
    return jsonify(question)


@app.route("/questiontest/<int:question_id>",methods=['DELETE'])
def delete_question(question_id):
    global ques
    ques = [q for q in ques if q['id'] != question_id]
    return '', 204



# Importing sources from Sources.py
from sources import Source

# Path to the Sources.py file
sources_file_path = 'sources.py'

# Function to save changes to Sources.py
def save_sources(updated_sources):
    with open(sources_file_path, 'r') as file:
        lines = file.readlines()
    
    with open(sources_file_path, 'w') as file:
        for line in lines:
            if line.strip().startswith('sources ='):
                file.write(f'sources = "{updated_sources}"\n')
            else:
                file.write(line)

@app.route('/sourceupdate', methods=['POST'])
def update_entry():
    try:
        text = request.json.get('text')
        new_desc = request.json.get('new_desc')

        if not text or not new_desc:
            return jsonify({"error": "Missing 'text' or 'new_desc' in request"}), 400

        entries = Source.split(', ')
        for i, entry in enumerate(entries):
            if entry.startswith(text + ':'):
                entries[i] = f"{text}: {new_desc}"
                updated_sources = ', '.join(entries)
                save_sources(updated_sources)
                return jsonify({"message": "Entry updated successfully"}), 200

        return jsonify({"error": "Entry not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/sourcedelete', methods=['DELETE'])
def delete_entry():
    try:
        text = request.json.get('text')

        if not text:
            return jsonify({"error": "Missing 'text' in request"}), 400

        entries = Source.split(', ')
        updated_entries = [entry for entry in entries if not entry.startswith(text + ':')]

        if len(entries) == len(updated_entries):
            return jsonify({"error": "Entry not found"}), 404

        updated_sources = ', '.join(updated_entries)
        save_sources(updated_sources)
        return jsonify({"message": "Entry deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/sourceget",methods=['GET'])
def get_sources():
    return jsonify(Source.split(', '))

@app.route("/query", methods=["POST"])
def query():
    """Endpoint to handle queries."""
    data = request.json
    str_input = data.get("query", "")
    userid = data.get("userid", "")

    if str_input:
        # memory = ChatMemoryBuffer.from_defaults(
        #     token_limit=8000,
        #     chat_store=chat_store,
        #     chat_store_key=userid,
        # )
        print("id : "+ userid)
    #affiliate links
        Gadgets = " OnePlus Buds Z3: https://amzn.in/d/6B1PBMy, Sony TWS WF-1000XM5: https://amzn.in/d/557hst5, Panasonic New 2024 EU Series AC:  https://amzn.in/d/fHD5sbn, itel s24: https://www.itel-india.com/product/s24/ , IMO Z7: https://amzn.in/d/238N4gZ , IQOO Z9X: https://www.iqoo.com/in/products/param/z9x_5g , Oneplus go tablet: https://www.oneplus.in/buy-oneplus-pad-go , Lava Pro smartwatch: https://shop.lavamobiles.com/products/prowatch-zn?variant=48783023800630 , OnePlus Nord CE4: https://amzn.in/d/acE6zdn , Redmi Note 13 Pro: https://amzn.in/d/iVNfkrq , Poco X6 Pro: https://amzn.in/d/i1xzdKa , OnePlus Nord 3 5G: https://amzn.in/d/i1xzdKa , Honor 90: https://amzn.in/d/cndn5L8 , Nothing Phone 2A: https://amzn.in/d/2qPZu1g , Sonos Beam 2 soundbar: https://amzn.in/d/2VLQzti , Logitech webcam 4K: https://amzn.in/d/4ntP1FJ"

        personality = "I am a digital clone of Abhishek Bhatnagar, powered by  Pluto AI proprietary technology. Abhishek is the founder and editor-in-chief of the tech website and media publication Gadgets To Use."
        
        #Source = " OnePlus Buds Z3: https://amzn.in/d/6B1PBMy, Sony TWS WF-1000XM5: https://amzn.in/d/557hst5, Panasonic New 2024 EU Series AC:  https://amzn.in/d/fHD5sbn, itel s24: https://www.itel-india.com/product/s24/ , IMO Z7: https://amzn.in/d/238N4gZ , IQOO Z9X: https://www.iqoo.com/in/products/param/z9x_5g , Oneplus go tablet: https://www.oneplus.in/buy-oneplus-pad-go , Lava Pro smartwatch: https://shop.lavamobiles.com/products/prowatch-zn?variant=48783023800630 , OnePlus Nord CE4: https://amzn.in/d/acE6zdn , Redmi Note 13 Pro: https://amzn.in/d/iVNfkrq , Poco X6 Pro: https://amzn.in/d/i1xzdKa , OnePlus Nord 3 5G: https://amzn.in/d/i1xzdKa , Honor 90: https://amzn.in/d/cndn5L8 , Nothing Phone 2A: https://amzn.in/d/2qPZu1g , Sonos Beam 2 soundbar: https://amzn.in/d/2VLQzti , Logitech webcam 4K: https://amzn.in/d/4ntP1FJ"
      #source link
       
  

       # response = chat_engine.chat(str_input)
        messagelist ="no"
        input = str_input
        response = ""
        updated_query = input




        #if empty list 
        if len(chat_store.get_messages(userid))==0:
           print("hello")
           response = query_engine.query(f"Given this query: {input} ." +"and answer it within 40 words")
        else: 
            print("input is : "+ input)
            print("history : " + chat_store.get_messages(userid)[0])
            check_follow_up = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
            messages=[
            {"role": "system", "content": "You are  a chat bot which checks if a query is a follow up to previous message or not"},
            {"role": "user", "content": f"Given previous chat history containing question asked by user and its answer by the system  : { chat_store.get_messages(userid)[0]}. \n"
                                                          " and Given that present user Query is :" + input  + "\n"
                                                         "check if present user query is a follow up message to previous message or not. Return yes or no"         
                 
                                                
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
           } ])
            

            is_follow_up = (check_follow_up.choices[0].message.content.strip()).lower()
            print("follow up is : " + is_follow_up)
            if is_follow_up =="yes":
             response = openai.chat.completions.create(
             model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
             messages=[
             {"role": "system", "content": "You are  a chat bot which rewrite the current query using the previous message to make sense as an individual message in concise manner"},
             {"role": "user", "content": f"Given previous chat history containing question asked by user and its answer by the system  : { chat_store.get_messages(userid)[0]}. \n"
                                                          " and Given that current user Query is :" + input  + "\n"
                                                         "rewrite the query using the relevant details from the previous message to make sense as an individual query and Return the updated query in format - Updated Query is <query> \n"         
                                                        
                                                
                                                                                #  " If the previous conversation and query are about differnt subject return query as it is else check this : If subect of query is vague and is related to previous chat conversion then update subject of query according to  subject of previous chat conversion in a concise manner and return the updated query in the format - Updated query : <query>"}
             } ]) 
             updated_query = extract_updated_query(response.choices[0].message.content.strip())
            else:
             updated_query = input




            
            
        print ("updated query : " + updated_query)
     #  print("chat history : " + chat_store.get_messages(userid)[0])
      #      print("message : " +  response.choices[0].message.content.strip())
        response = query_engine.query(f"Given this query: {input} ." +"and answer it within 40 words")
        messagelist = "User :" + updated_query + ", System : " + str(response)
        
       
        result = check_string(str(response))
      
        # chat management      
        chat_store.delete_last_message(userid)
        chat_store.add_message(userid, messagelist)
         

        print("result : " + result)
        if check_string(response.response) != "no":
        #  print('inside')
          source_link = model.generate_content(f"Given this query: {updated_query}. and \n " + "given string of key value pairs of topics with their respective links: " + Source + "\n" + "check if any topic is related to the query and if found return its respective link in the format - Source : <Link>. else return - NO")
          if source_link.text != "NO" :
             result = result + " " + source_link.text
      

       # if(link_check.text != "SKIP"):
        #    result = result + "\n" + link_check.text

        affiliate = find_key_value_pair(Gadgets, updated_query)
        if affiliate != "no" :
            result = result + "\n" + affiliate
            print("link: "+affiliate)



        new_string = ""
        

        if check_string(response.response) == "no":
         new_string = "no"
        else:
         for char in response.response.lower():
            if char.isalpha():
                new_string += char

      #  print("condition : " + new_string + "\n")
         
        if new_string == "no":
            # gemini_response = model.generate_content(
            #     f" if this: {str_input}, is about either about tech review or tech suggestions or tech tips & tricks then answer - Reach out at Zaidjunaid3 else if it is a tech related question then answer as usual else if it is not a tech related question then answer: Lets stick to tech."
            # )
            # sample_response = model.generate_content(
            #     f" Assume you are Digital clone of Gadgets to use that answers only to tech queries and greeting messages while following given conditions. Given this query: {str_input} \n.Answer this query using only one of the following five criterias: \n 1. If the query is a greeting message revert back saying Hello and that you would like to discuss technical topics. \n  2. Else If the query is about your personal information then respond with this context: {personality} \n 3. Else If the query is related to specific gadgets or recommendation of products then  respond while making user understand  that you would love to answer this query in detail and they can reach at this email for further details :  gadgetstouse@gmail.com.  \n 4. Else if it is a generic tech query answer it within 30 words \n 5.  Else reply to stick to technical topics only "
            # )


            fallback = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",  # or gpt-4 if you have access
            messages=[
            {"role": "system", "content": "You are digital clone of GTU, which is powered by Pluto.ai technology. You follow the following conditions : 1. You don't answer to non technology related queries 2. You reply to only generic tech related queries but don't reveal this in answer. 3. If you receive a query about specific tech gadgets or tech gadget recommendation or tech tips tricks then reply that you would love to answer this query in detail and they can reach at this email for further details :  gadgetstouse@gmail.com. 4. answer within 30 words"},
            {"role": "user", "content": f"Answer to this query: {updated_query} "
           } ])
            fallback_response = fallback.choices[0].message.content.strip()
            print("loop : "  + fallback_response) 
          
            result

          
            result = fallback_response
           
         
        return jsonify({"response": result})
    
    return jsonify({"response": "No input provided"}), 400







@app.route("/questions", methods=["POST"])
def questions():
    topic_data = request.json
    topic_kw = topic_data.get("topic", "")
    userid = topic_data.get("userid", "default_user")
    print(topic_kw)
    
    Info = query_engine.query(f"tell about: {topic_kw} ")
    messagelist = "question :" + topic_kw + ", answer : " + str(Info)
    print(Info)


    chat_store.delete_last_message(userid)
    chat_store.add_message(userid, messagelist)


    response_1 = model.generate_content(
        f"Given this text : {Info}. Generate four short questions that can be answered by using the text , without mentioning about the text in this format Suggested questions : <question list in numeric pointers and single line>"
    )

    questions=response_1.text.strip()
    questions = questions.replace("Suggested questions :\n", "")
    # questions = questions.replace("Suggested questions:\n", "")
    # questions = questions.replace("Suggested questions : \n", "")
    # questions = questions.replace("Suggested questions: \n", "")
    # questions = questions.replace("Suggested questions :\n\n", "")
    # questions = questions.replace("Suggested questions:\n\n", "")
    # questions = questions.replace("Suggested questions : \n\n", "")
    # questions = questions.replace("Suggested questions: \n\n", "")
    # questions = questions.replace("**Suggested questions:**\n\n", "")
    questions = remove_leading_newline(questions)

    
    return jsonify({"questions": questions})

# Error handling in case something goes wrong
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e),
        "message": "An error occurred while processing your request."
    }
    return jsonify(response)




@app.route("/suggest-questions", methods=["GET"])
def suggest_questions():
    shuffled_questions = ques.copy()
    random.shuffle(shuffled_questions)
    
    formatted_questions = []
    for index, question in enumerate(shuffled_questions):
        formatted_questions.append(f"{index + 1}. {question['question']}")
    
    return jsonify({"questions": "\n".join(formatted_questions)})


# Error handling in case something goes wrong
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e),
        "message": "An error occurred while processing your request."
    }
    return jsonify(response)


@app.route("/save", methods=["POST"])
def save_to_system():
    try:
        data = request.json
        save_info = data.get("user_query", "")
        save_text_to_file(save_info, "save.txt")
        return jsonify("success"), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify("error"), 500



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))