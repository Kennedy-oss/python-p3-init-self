#!/usr/bin/env python3

# In lib/dog.py

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

fido = Dog("Fido")  # Breed will be "Mutt"
buddy = Dog("Buddy", "Golden Retriever")  # Breed will be "Golden Retriever"

