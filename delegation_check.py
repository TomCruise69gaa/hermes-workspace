#!/usr/bin/env python3
from datetime import datetime, timezone

print(f"UTC Timestamp: {datetime.now(timezone.utc).isoformat()}")
