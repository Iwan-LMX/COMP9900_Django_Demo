from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from django.conf import settings
# 初始化模型
llm = ChatGoogleGenerativeAI(model=settings.MODEL_NAME, google_api_key=settings.GOOGLE_API_KEY)
prompt = ChatPromptTemplate.from_template("Ask the following：{question}")
chain = prompt | llm | StrOutputParser()
@api_view(['POST'])
@csrf_exempt
def ask_question(request):
    question = request.data.get('question', '')
    response = chain.invoke({"question": question})
    return JsonResponse({"response": response})