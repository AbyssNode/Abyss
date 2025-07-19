# core_registry.py

REGISTRY = {}

def register_module(name, status="inactive"):
    REGISTRY[name] = status

def activate_module(name):
    if name in REGISTRY:
        REGISTRY[name] = "active"

def get_status():
    return REGISTRY
