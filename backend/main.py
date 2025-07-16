from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from backend.generator import generate_readme

app = FastAPI()

# Add CORS middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

class ReadmeRequest(BaseModel):
    name: str
    version: str
    description: str
    usage_steps: str
    stack: str
    audience: str
    author: str
    showcase_video: str

# Serve the HTML file at the root
@app.get("/")
async def read_index():
    return FileResponse('frontend/index.html')

@app.post("/generate")
async def generate(request: ReadmeRequest):
    readme_text = generate_readme(
        request.description, 
        request.stack, 
        request.audience,
        request.name,
        request.version,
        request.usage_steps,
        request.author,
        request.showcase_video
    )
    return {"readme": readme_text}
