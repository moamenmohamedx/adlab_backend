"""Data grid agent with AI-powered CRUD operations."""

import os
from textwrap import dedent

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.ag_ui import StateDeps
from ag_ui.core import EventType, StateSnapshotEvent

from persistence import save_state

# Load environment variables
load_dotenv()

# Verify API key
if not os.getenv("OPENROUTER_API_KEY"):
    raise ValueError("OPENROUTER_API_KEY not found in environment variables!")

# Model configuration
MODEL = "openrouter:openai/gpt-4o-mini"


# =============================================================================
# Data Models
# =============================================================================

class GridRow(BaseModel):
    """Single row in the data grid."""
    
    id: int = Field(..., description="Unique numeric identifier")
    product_name: str = Field(..., description="Product name")
    product_type: str = Field(..., description="Product category")
    key_points: str = Field(..., description="Key product description/notes")


class GridState(BaseModel):
    """Complete grid state with metadata."""
    
    rows: list[GridRow] = Field(
        default_factory=list,
        description="All grid rows"
    )
    next_id: int = Field(
        default=1,
        description="Next available ID for new rows"
    )


# =============================================================================
# Agent Configuration
# =============================================================================

agent = Agent(
    model=MODEL,
    deps_type=StateDeps[GridState],
    system_prompt=dedent("""
        You are a data grid assistant. Help users manage their sales data grid.
        
        You can:
        - Add new rows with product name, type, and key points
        - Update existing rows by ID
        
        Always respond conversationally and confirm actions taken.
        When adding rows, include the new row's ID in your response.
        When updating rows, confirm which row was updated.
        
        Be helpful and proactive. If the user asks about the data,
        describe what you can help them do with it.
    """).strip()
)


# =============================================================================
# Agent Tools
# =============================================================================

@agent.tool
async def add_row(
    ctx: RunContext[StateDeps[GridState]],
    product_name: str,
    product_type: str,
    key_points: str
) -> StateSnapshotEvent:
    """Add a new row to the data grid."""
    state = ctx.deps.state
    
    # Generate unique ID
    new_id = state.next_id
    state.next_id += 1
    
    # Create and append row
    new_row = GridRow(
        id=new_id,
        product_name=product_name,
        product_type=product_type,
        key_points=key_points
    )
    state.rows.append(new_row)
    
    # Persist to disk
    save_state(state)
    
    return StateSnapshotEvent(
        type=EventType.STATE_SNAPSHOT,
        snapshot=state,
    )


@agent.tool
async def update_row(
    ctx: RunContext[StateDeps[GridState]],
    row_id: int,
    product_name: str | None = None,
    product_type: str | None = None,
    key_points: str | None = None
) -> StateSnapshotEvent:
    """Update specific fields in an existing row."""
    state = ctx.deps.state
    
    # Find row by ID
    row = next((r for r in state.rows if r.id == row_id), None)
    if not row:
        # Gracefully handle missing row
        return StateSnapshotEvent(
            type=EventType.STATE_SNAPSHOT,
            snapshot=state,
        )
    
    # Update provided fields
    if product_name is not None:
        row.product_name = product_name
    if product_type is not None:
        row.product_type = product_type
    if key_points is not None:
        row.key_points = key_points
    
    # Persist to disk
    save_state(state)
    
    return StateSnapshotEvent(
        type=EventType.STATE_SNAPSHOT,
        snapshot=state,
    )
