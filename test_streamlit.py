#!/usr/bin/env python3
"""Test if Streamlit is installed"""
try:
    import streamlit as st
    print("✅ Streamlit está instalado!")
    print(f"Versão: {st.__version__}")
except ImportError:
    print("❌ Streamlit não está instalado")
    exit(1)
