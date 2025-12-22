import sys
import os

# CRITICAL FIX: Set UTF-8 encoding for Windows console to prevent charmap errors
if sys.platform == 'win32':
    try:
        # Force UTF-8 encoding for stdout/stderr
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass
    # Set environment variable for Python IO encoding
    os.environ['PYTHONIOENCODING'] = 'utf-8'

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from agent import ProverbsState, StateDeps, agent

# Create the AG-UI ASGI app with CORS middleware built-in
# AGUIApp extends Starlette and accepts middleware parameter natively
app = agent.to_ag_ui(
    deps=StateDeps(ProverbsState()),
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3000"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
)

if __name__ == "__main__":
    # run the app
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

