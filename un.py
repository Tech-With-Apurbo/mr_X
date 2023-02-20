import os, sys
try:
    __import__("mrxyz").menu()
except Exception as e:
    exit(str(e))
