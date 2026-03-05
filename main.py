from fastapi import FastAPI, UploadFile, File
from schemas import ChatRequest
from agents.idea_agent import handle_idea
from agents.stack_agent import handle_stack
from agents.code_agent import handle_code
from agents.debug_agent import handle_debug
from advanced_debug.advanced_debug_agent import handle_advanced_debug
#from advanced_debug.ocr_service import extract_text_from_image
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def detect_intent(message: str) -> str:
    msg = message.lower()

    if "error" in msg or "exception" in msg or "traceback" in msg:
        return "debug"

    elif "tech stack" in msg or "stack" in msg:
        return "stack"

    elif "code" in msg or "generate" in msg or "build api" in msg:
        return "code"

    else:
        return "idea"


@app.post("/chat")
async def chat(request: ChatRequest):
    intent = detect_intent(request.message)

    if intent == "debug":
        response = handle_debug(request.message)

    elif intent == "stack":
        response = handle_stack(request.message)

    elif intent == "code":
        response = handle_code(request.message)

    else:
        response = handle_idea(request.message)

    return {
        "intent": intent,
        "response": response
    }


# ✅ Advanced Debug (Text Input)
@app.post("/advanced-debug")
async def advanced_debug(request: ChatRequest):

    response = await handle_advanced_debug(request.message)

    return {"response": response}

from services.gemini_service import extract_text_with_gemini

@app.post("/advanced-debug-upload")
async def advanced_debug_upload(file: UploadFile = File(...)):

    image_bytes = await file.read()

    extracted_text = extract_text_with_gemini(image_bytes)

    response = await handle_advanced_debug(extracted_text)

    return {
        "extracted_text": extracted_text,
        "response": response
    }
# ✅ Advanced Debug (Screenshot Upload)
