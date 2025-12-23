"""JSON file persistence for GridState."""

import json
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agent import GridState

# Configuration
STATE_FILE = Path(__file__).parent.parent / "data" / "grid_state.json"


def load_initial_state() -> "GridState":
    """
    Load GridState from JSON file.
    
    Returns default state with sample data if file doesn't exist.
    """
    # Import here to avoid circular dependency at module level
    from agent import GridState, GridRow
    
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return GridState(**data)
        except (json.JSONDecodeError, ValueError):
            pass  # Fall through to default
    
    # Return default state with sample data
    return GridState(
        rows=[
            GridRow(
                id=1,
                product_name="Alpha Project",
                product_type="Software",
                key_points="Cloud-native scalable solution with multi-region support."
            ),
            GridRow(
                id=2,
                product_name="Beta Stream",
                product_type="Service",
                key_points="Real-time data pipeline processing with low latency architecture."
            ),
            GridRow(
                id=3,
                product_name="Gamma Ray",
                product_type="Hardware",
                key_points="High Performance: 80% revenue increase in Q4."
            ),
            GridRow(
                id=4,
                product_name="Delta Force",
                product_type="Software",
                key_points="Advanced endpoint security suite with zero-trust implementation."
            ),
            GridRow(
                id=5,
                product_name="Epsilon Edge",
                product_type="Hardware",
                key_points="Edge computing units featuring ultra-low power consumption."
            ),
            GridRow(
                id=6,
                product_name="Zeta Zone",
                product_type="Service",
                key_points="Consulting framework for virtualized zone architecture."
            ),
            GridRow(
                id=7,
                product_name="Eta Energy",
                product_type="Utility",
                key_points="Renewable energy grid management optimization algorithms."
            ),
            GridRow(
                id=8,
                product_name="Theta Time",
                product_type="Consumer",
                key_points="Smart scheduling app with AI-powered time optimization."
            ),
            GridRow(
                id=9,
                product_name="Iota Innovation",
                product_type="R&D",
                key_points="Early stage interface prototype showing promising user engagement."
            ),
        ],
        next_id=10
    )


def save_state(state: "GridState") -> None:
    """Save GridState to JSON file."""
    # Ensure data directory exists
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Write state using model_dump() for Pydantic serialization
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state.model_dump(), f, indent=2)
