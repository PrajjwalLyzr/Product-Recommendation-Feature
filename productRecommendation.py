from lyzr import ChatBot
from pathlib import Path



def recommendation_analyzr(material,budget,automation_level,process, power, weight):
    chatbot = ChatBot.pdf_chat(
        input_files=[Path("./data/Product_data - data.pdf")]
    )

    response = chatbot.chat(f"Analyze the pdf file and provide a recommeded product 'name' based on these features: {material},{process},{budget},{automation_level},{power},{weight},[!Important] just provide the 'name' from the pdf file, nothing else")

    return response.response


