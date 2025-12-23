"""FastAPI application entry point for data grid agent."""

import sys
import os

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from agent import agent, StateDeps
from persistence import load_initial_state

# Windows console UTF-8 encoding fix
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass
    os.environ['PYTHONIOENCODING'] = 'utf-8'


# Create AG-UI ASGI application
app = agent.to_ag_ui(
    deps=StateDeps(load_initial_state()),
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
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
