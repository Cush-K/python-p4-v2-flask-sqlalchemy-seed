#!/usr/bin/env python3
#server/seed.py

import random
from faker import Faker

from app import app
from models import db, Pet

fake =Faker()

with app.app_context():
    
    Pet.query.delete()
    
    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add some Pet instances to the list
    for n in range(10):
        pet = Pet(name=fake.first_name(), species=random.choice(species))
        pets.append(pet)
    
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()