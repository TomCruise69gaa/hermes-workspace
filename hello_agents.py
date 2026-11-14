#!/usr/bin/env python3
"""Basic test script for hello_agents functionality."""

import datetime
import platform
import sys

def test_imports():
    """Test basic Python imports work."""
    print("Testing basic imports...")
    import os
    import json
    print("  ✓ All basic imports successful")

def test_print_output():
    """Test that stdout works correctly."""
    print("Testing print output...")
    print("Hello, hello_agents!")
    print(f"Current time: {datetime.datetime.now()}")

def test_system_info():
    """Test system information is accessible."""
    print("Testing system info...")
    print(f"  OS: {platform.system()}")
    print(f"  Python version: {sys.version}")

def main():
    """Run all tests."""
    print("=" * 50)
    print("hello_agents.py - Basic Functionality Test")
    print("=" * 50)
    print()
    
    test_imports()
    print()
    
    test_print_output()
    print()
    
    test_system_info()
    
    print()
    print("=" * 50)
    print("All tests passed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
